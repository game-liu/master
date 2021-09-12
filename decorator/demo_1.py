import time


def decorate(func):
    start = time.time()
    a = func()
    time.sleep(5)
    end = time.time()
    print(f"all_time:{end - start}")
    return a


def cal_data():
    res = []
    for i in range(1, 100):
        if i % 2 == 1:
            res.append(i)
    print(res)
    return res


if __name__ == '__main__':
    a = decorate(cal_data)
    print(a)
