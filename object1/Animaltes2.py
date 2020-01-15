class Animal:
    x = 123

    def __init__(self):
        self.y = 456

    def shout(self):
        print('Animal shuts ')


class Cat(Animal):
    x = 'abc'

    def __init__(self):
        self.y = 'xyz'

    def shout(self):
        print('Maio')


a = Animal()
a.shout()

c = Cat()
c.shout()
print(c.x)
print(c.y)
print(a.y)


