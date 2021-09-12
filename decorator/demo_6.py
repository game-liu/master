import time


def time_decorate(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        time.sleep(1)
        end = time.time()
        print(f"all_time:{end - start}")
        return ret  # 原函数返回值
    return wrapper

def log_decorate(func):
    def wrapper():
        start = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        ret = func()
        end = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(f"logging: func:{func.__name__} runs from {start} to {end}")
        return ret

    return wrapper


@time_decorate
@log_decorate
def count_data(n=100):
    count = 0
    for i in range(n):
        if i % 2 == 1:
            count += 1
    print(f'count:{count}')
    return count

if __name__ == '__main__':
    ret = count_data()
    print(ret)