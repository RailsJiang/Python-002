import time


def count_time(func):
    def int_time(*args, **kwargs):
        start_time = time.time()
        func()
        end_time = time.time()
        total_time = end_time - start_time
        print('程序运行共计%s秒' % total_time)
    return int_time


@count_time
def main():
    print('>>>>开始计算函数运行时间')
    for i in range(1, 1000):
        for j in range(i):
            print(j)


if __name__ == '__main__':
    main()
