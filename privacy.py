class PrivacyExp(Exception):
    pass


class Privacy:
    def __setattr__(self, attr, val):
        if attr in self.privates:
            raise AttributeError(attr + ' not allowed')
        else:
            self.__dict__[attr] = val


class Test1(Privacy):
    privates = ['age']


class Test2(Privacy):
    privates = ['name', 'pay']

    def __init__(self):
        self.__dict__['name'] = 'Tom'
        # self.name = 'Tom'


x = Test1()
y = Test2()

x.name = 'Bob'
print(x.name)
# y.name = 'Sue'
print(y.name)

y.age = 30
print(y.age)
# x.age = 40
