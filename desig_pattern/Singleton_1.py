class Singleton:
    __obj = None
    __init = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = super(Singleton, cls).__new__(cls)
        return cls.__obj

    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(cls, '_instance'):
    #         cls._instance = super(Singleton, cls).__new__(cls)
    #     return cls._instance

    def __init__(self, name):
        if Singleton.__init:
            print('init.....')
            self.name = name
            Singleton.__init = False


a = Singleton('aaa')
print(a)
# b = Singleton('''bbb''')
