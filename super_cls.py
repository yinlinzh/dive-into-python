from abc import ABCMeta, abstractmethod


class Super(metaclass=ABCMeta):
    def method(self):
        print('in Super.method')

    def delegate(self):
        self.action()

    @abstractmethod
    def action(self):
        ...


class Inheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        print('in Replacer.method')


class Extender(Super):
    def method(self):
        print('Starting Extender.method')
        Super.method(self)
        print('Ending Extender.method')


class Provider(Super):
    def action(self):
        print('in Provider.action')


if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()

    print('\nProvider...')
    x = Provider()
    x.delegate()
