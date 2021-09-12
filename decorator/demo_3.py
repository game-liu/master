import time


def decorate(func):
    def wrapper():
        start = time.time()
        func()
        time.sleep(2)
        end = time.time()
        print(f"all_time:{end - start}")

    return wrapper


@decorate
def cal_data():
    res = []
    for i in range(100):
        if i % 2 == 1:
            res.append(i)
    print(res)
    return res


if __name__ == '__main__':
    ret = cal_data()
