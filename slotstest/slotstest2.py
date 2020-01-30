class A:
    def __init__(self,x ):
        self.y = x

    def __add__(self, other):
        print('A__add__')
        if hasattr(other,'x'):
            x = self.x + other.x
        else :
            x = self.x + other
        self.x = x
        return self

    def __iadd__(self, other):
        print('A__iadd__')
        return A(self.x + other.x)

    def __radd__(self, other): #反向相加
        print('A__radd__')
        return self + other

    __radd__ = __add__


class B :
    def __init__(self):
        self.x = 5

a = A()
b = B()
a + b
b + a





