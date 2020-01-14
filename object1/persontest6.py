class Person:
    def __init__(self,name,age):
        self._name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        self.__age = age

    @age.deleter
    def age(self):
        print('del age ')


tom = Person('tom',20)
print(tom.age)
tom.age = 30
print(tom.age)
del tom.age












