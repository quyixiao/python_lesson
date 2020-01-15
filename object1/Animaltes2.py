
# super()可以访问到父类的属性，但是不能访问
#
class Animal:
    x = 123

    def __init__(self):
        self.y = 456

    def shout1(self):
        print('----------1111111111111111----------')

    def shout(self):
        print('Animal shuts ' , self.shout1())


    def speek(self):
        print('Animal speek ',self.__class__.__name__ ,self.y)


    @classmethod
    def showx(cls):
        print(cls.x)

    @classmethod
    def showy(cls):
        print(cls.y)



class Cat(Animal):
    x = 'abc'
    def __init__(self):
        self.y = 'xyz'

    showx = list

    def shout1(self):
        print('----------2222222222222222----------')
    def shout(self):
        print('--------------------')
        Animal.shout(self)


    def speek(self):
        print('Cat speek ' )
        super().speek()

    @classmethod
    def showx(cls):
        print(cls.__base__.x)


    @classmethod
    def showy(cls):
        print('--------------------------------------')
        print(cls.y)



#a = Animal()
#a.shout()

c = Cat()
c.shout()
c.speek()
print(c.x)
print(c.y)
b = c.showx()
print(type(b))
#c.showy()
#print(a.y)


