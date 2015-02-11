class Adder:
    def __init__(self, val=0):
        self.data = val

    def __add__(self, other):
        self.data += other


class AdderRepr(Adder):
    def __repr__(self):
        return 'REPR version: AdderRepr(%s)' % self.data

    def __str__(self):
        return 'STR version: AdderRepr(%s)' % self.data


X = AdderRepr(2)
X + 13
print(X)

print(__name__)
print(__file__)
