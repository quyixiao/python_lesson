import inspect

class TypeCheck:
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

class Person:
    name = TypeCheck()
    age = TypeCheck()

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

print(inspect.signature(Person))
print(inspect.signature(Person).parameters)

# 这种方法的
p1 = Person('tom', 20)
p2 = Person('jerry', '38')
