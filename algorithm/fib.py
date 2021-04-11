def fib(n: int) -> int:
    if n <= 0:
        return 1
    else:
        return n * fib(n - 1)


if __name__ == '__main__':
    ret = fib(5)
    print(ret)
