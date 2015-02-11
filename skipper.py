class SkipIterator:
    def __init__(self, wrapper):
        self.wrapper = wrapper
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapper):
            raise StopIteration()
        else:
            res = self.wrapper[self.offset]
            self.offset += 2
            return res


class SkipObject:
    def __init__(self, wrapper):
        self.wrapper = wrapper

    def __iter__(self):
        return SkipIterator(self.wrapper)


def main():
    alpha = 'abcdef'
    skipper = SkipObject(alpha)
    i = iter(skipper)
    print(next(i), next(i), next(i), sep=' - ')
    for x in skipper:
        for y in skipper:
            print(x + y, end=' | ')

if __name__ == '__main__':
    main()
