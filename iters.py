class Square:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration()
        self.value += 1
        return self.value ** 2


class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, index):
        print('get[%s]: ' % index, end='')
        return self.data[index]

    # def __iter__(self):
    #     print('iter=> ', end='')
    #     self.idx = 0
    #     return self

    def __next__(self):
        print('next:', end='')
        if self.idx == len(self.data):
            raise StopIteration()
        res = self.data[self.idx]
        self.idx += 1
        return res

    # def __contains__(self, x):
    #     print('contains: ', end='')
    #     return x in self.data


X = Iters([1, 2, 3, 4, 5])
print(3 in X)
for i in X:
    print(i, end='|')

print()
print([i ** 2 for i in X])
print(list(map(bin, X)))

I = iter(X)
while True:
    try:
        print(next(I), end=' @ ')
    except StopIteration:
        break

print()
