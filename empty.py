class Empty:
    # job = 'developer'
    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)

X = Empty()
print(X.age)
print(X.job)
