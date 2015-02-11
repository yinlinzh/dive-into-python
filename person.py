class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def __str__(self):
        return '[Person %s, %s]' % (self.name, self.pay)

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay *= (1 + percent)


class Manage(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def give_raise(self, percent, bonus=.10):
        Person.give_raise(self, percent + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)

    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.name.split()[-1])
    sue.pay *= 1.10
    print(sue.pay)
    print(sue)

    tom = Manage('Tom Jones', 50000)
    tom.give_raise(.1)
    print(tom.last_name())
    print(tom)
