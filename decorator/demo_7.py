def information(value):
    def decorate(func):
        def wrapper(*args, **kwargs):
            print(f"now the value is {value}")
            func(*args, **kwargs)
        return wrapper
    return decorate

@information(value='IS MY')
def func():
    print('func starting')
    pass


if __name__ == '__main__':
    func()