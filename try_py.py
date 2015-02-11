# import sys

# print(sys.argv)
# print(sys.version)

# print("hello world")
# print(1 + 3)
# print(2 ** 10)


# a = [1.11,
#      2.22,
#      3.33]

# x = 'spam'
# while x:
#     _, *x = x
#     print(x, end=' ')
# else:
#     print('not touch break')

# while False:
#     print('In False while')
# else:
#     print('In False else')


# def f1():
#     X = 87
#     def f2():
#         print(X)
#     return f2

# action = f1()
# action()

# def maker(N):
#     def func(base):
#         return base ** N
#     return func

# power5 = maker(6)
# print(power5(2))

# def f1():
#     X = 8
#     f2(X)

# def f2(X):
#     print(X)

# f1()

# print('-' * 20)

# def makeAction():
#     return [lambda x, i = i: i ** x for i in range(5)]

# acts = makeAction()
# for i in range(5):
#     print(acts[i](2))

# def f(*args):
#     print(args)

# f()
# f(1)
# f(1,2,3,5)

# def g(**args):
#     print(args)

# g(a=1, b=2, c=3)
# # g(1)

# def f(a, b, c, d): print(a, b, c, d, sep='=')
# f(*(1,2,3,9))

class C1: ...

class C2: ...

class C3(C1, C2):
    def __init__(self, who):
        self.name = who
        print(self.name)

I1 = C3('bob')
I2 = C3('mel')
print(C3.__dict__)
print(C3.__bases__)
print('-' * 20)

class X:
    def setdata(self, data):
        self.data = data
    def display(self):
        print(self.data)

x = X()
x.setdata('abc')
x.display()
y = X()

print(x.__dict__)
print(y.__dict__)
print(x.__class__)
