import inspect


class TypeCheck:
    def __init__(self, key, type):
        self.key = key
        self.type = type

    def __get__(self, instance, owner):
        print('--------------------------------')
        return self.__dict__[self.key]

    def __set__(self, instance, value):
        print(self, instance, value)
        if not isinstance(value, self.type):
            raise TypeError('{} {} '.format(self.key, self.type))
        self.__dict__[self.key] = value


def typeassert(cls):
    print(inspect.signature(cls))
    params = inspect.signature(cls).parameters
    print(params)
    for name, param in params.items():
        print(name, '----------------', param, '-------', param.annotation)
        if param.annotation != param.empty:
            setattr(cls, name, TypeCheck(name, param.annotation))
    return cls


@typeassert
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


# 这种方法的
p1 = Person('tom', 123)







