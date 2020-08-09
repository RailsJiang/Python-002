import subprocess
import telnetlib
import sys, getopt
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import Pool


def check_port(ip):
    """
    检查指定ip的指定端口是否可以访问
    :param ip:
    :param port:
    :return:
    """

    server = telnetlib.Telnet()
    try:
        server.open(ip[0], ip[1], timeout=5)
        print(f"ip:port -> {ip[0]}:{ip[1]} is open!")
    except Exception:
        return False
    finally:
        server.close()


def check_all_ports(ip, n):
    """
    输入ip，检查所有端口
    :param ip:
    :param n:
    :return:
    """
    port_list = [(ip, port) for port in range(1, 1025)]

    with ThreadPoolExecutor(n) as executor:
        executor.map(check_port, port_list)


def get_opt(argv, optarg):
    try:
        opts, args = getopt.getopt(argv, "hi:m:w:n:", ["ip=", "ofile="])
        print(opts)
    except getopt.GetoptError:
        print('usage: python test.py [-i|--ip ip] [-m proc|thread] [-v] [-w outputfile]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('usage: python test.py [-i|--ip ip] [-m proc|thread] [-v] [-w outputfile]')
            sys.exit()
        elif opt in ("-m"):
            optarg['ismultiprocess'] = True
            optarg['multimode'] = arg
            print(f"multimode: {opt['multimode']}: {opt['ismultiprocess']}")
        elif opt in ("-n"):
            optarg['multinum'] = int(arg)
            print(f"concurent_num: {optarg['multinum']}")
        elif opt in ("-i", "--ip"):
            optarg['ip'] = arg
            print(f"ip: {optarg['ip']}")
    if optarg['ip'] == '':
        print('usage: python test.py [-i|--ip ip] [-m proc|thread] [-v] [-w outputfile]')
        sys.exit()


def main(argv):
    opt = {
        'ismultiprocess': False,
        'multimode': '',
        'multinum': 1,
        'outfile': '',
        'ip': '',
    }
    get_opt(argv, opt)

    ip = opt['ip']

    check_all_ports(ip, opt['multinum'])


if __name__ == "__main__":
   main(sys.argv[1:])