# 单继承
class Animal:
    x = 123

class Cat(Animal):
    x = 'abc'

class Dog(Animal):
    x = 'Dog'

class CarField(Cat,Dog): # order (MRO) for bases object, Cat, Dog
    pass

print(Cat.mro())
print(Cat.__mro__)
print(Dog.mro())
print(Dog.__mro__)

print(CarField.mro())
print(CarField.__mro__)

print(CarField.x)



