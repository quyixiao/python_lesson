class Animal:
    def shout(self):
        print('Animal shuts ')


class Cat(Animal):
    def shout(self):
        print('Maio')


a = Animal()
a.shout()


c = Cat()
c.shout()