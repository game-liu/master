class Singleton(object):
    __is_init = False

    def __new__(cls, *args, **kwargs):
        print('new....')
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, name):
        if not Singleton.__is_init:
            print('init.....')
            Singleton.__is_init = True


single_1 = Singleton('1')
print(single_1)
single_2 = Singleton('2')
print(single_2)
