import time


def cal_data():
    res = []
    for i in range(100):
        if i % 2 == 1:
            res.append(i)
    print(res)
    return res


# 闭包函数的参数和返回值都是函数
# 闭包函数是对原函数功能的拓展
# 闭包函数本来也是一个函数
def decorate(func):
    def wrapper():
        start = time.time()
        func()
        time.sleep(2)
        end = time.time()
        print(f"all_time:{end - start}")

    return wrapper


if __name__ == '__main__':
    result = decorate(cal_data)
    result()
