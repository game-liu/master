# 有返回值
# 有参数

import time


def decorate(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        time.sleep(1)
        end = time.time()
        print(f"all_time:{end - start}")
        return ret  # 原函数返回值
    return wrapper


def count_data(n=100):
    count = 0
    for i in range(n):
        if i % 2 == 1:
            count += 1
    return count


# 对于有返回值的函数，调用闭包增强后，不能成功返回，但是增强了原函数的功能
# 对于含有参数的函数，不能进行传参
if __name__ == '__main__':
    print(count_data(n=1000))
    print('--------------- 可以接受到返回值-------------------------------')
    res = decorate(count_data)
    print(res(n=1000))