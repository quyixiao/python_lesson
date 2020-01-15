#  格式定义如下
#  class 子类名中（基类1 [,基类2,....]）
#  如果类的定义，没有基类的列表，等同埋于继承自 object,在 python3 中
#

class Animal:
    def shout(self):
        print(self.__class__.__name__ + " to shut ")

class Cat(Animal):
    pass

class Dog(Animal):
    pass

cat = Cat()
cat.shout()


dog = Dog()
dog.shout()



print(Dog.mro())
print(Dog.__mro__)
