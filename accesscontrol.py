class AccessControl:
    def __setattr__(self, attr, val):
        if attr == 'age':
            self.__dict__[attr] = val
        else:
            raise AttributeError(attr + ' not allowed')

# X = AccessControl()
