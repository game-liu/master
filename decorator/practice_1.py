def wrapper1(func1):
    print('set func1')

    def imporved_func1():
        print('call func1')
        func1()
    return imporved_func1


def wrapper2(func2):
    print('set func2')

    def improved_func2():
        print('call func2')
        func2()

    return improved_func2


@wrapper1
@wrapper2
def func():
    print('call func')
    pass


if __name__ == '__main__':
    # 将装饰器闭包
    # 1.
    # test_func = wrapper1(wrapper2(func))

    # 2.
    # print(func.__name__)
    # test_func = wrapper2(func)
    # print(test_func.__name__)
    # test_func = wrapper1(test_func)
    # print(test_func.__name__)
    # test_func()

    func()
    print('-------------')
    func()
