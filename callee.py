class Callee:
    def __call__(self, *pargs, **kwargs):
        print('Called: ', pargs, kwargs)


c = Callee()
c(1, 2, 3)
c(1, 2, 3, x=4, y=5)
