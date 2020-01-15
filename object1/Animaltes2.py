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



class Cat(Animal):
    x = 'abc'
    def __init__(self):
        self.y = 'xyz'


    def shout1(self):
        print('----------2222222222222222----------')
    def shout(self):
        print('--------------------')
        Animal.shout(self)


    def speek(self):
        print('Cat speek ' )
        super().speek()



#a = Animal()
#a.shout()

c = Cat()
c.shout()
c.speek()
print(c.x)
print(c.y)
#print(a.y)


