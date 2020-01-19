import inspect

class TypeCheck:
    def __init__(self,key,type):
        self.key = key
        self.type = type

    def __get__(self, instance, owner):
        print('--------------------------------')
        #return instance.__dict__[self.key]
        return self.__dict__[self.key ]

    def __set__(self, instance, value):
        print(self,instance,value)
        if not isinstance(value,self.type):
            raise TypeError('{} {} '.format(self.key,self.type))
        #instance.__dict__[self.key] = value
        self.__dict__[self.key] = value


class Person:
    name = TypeCheck('name',str)
    age = TypeCheck('age',int )

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


print(inspect.signature(Person))
print(inspect.signature(Person).parameters)

# 这种方法的
p1 = Person('tom', 20)
print(p1.__dict__)
print(Person.__dict__)
print('*'*20)
#p2 = Person('jerry', '38')
