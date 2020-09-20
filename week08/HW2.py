def myMap(func, iter):
    """
    自定义map()方法
    :param func:
    :param iter:
    :return:
    """
    for item in iter:
        yield func(item)


### 测试程序

def square(x):
    return x ** 2

print(list(myMap(square, [1,2,3,4,5])))