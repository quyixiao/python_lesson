class A:
    def __init__(self):
        self.a1 = 'a1'
        print('A__init__')


class B:
    x = A()
    def __init__(self):
        print('B___init__')


print('-' * 20)
print(B.x.a1)
print('='*20)
b = B()
print(b.x.a1)










