import inspect


class TypeCheck:
    def __init__(self, key, type):
        self.key = key
        self.type = type

    def __get__(self, instance, owner):
        print('--------------------------------')
        if instance is not None:
            return self.__dict__[self.key]
        return self

    def __set__(self, instance, value):
        print(self, instance, value)
        if not isinstance(value, self.type):
            raise TypeError('{} {} '.format(self.key, self.type))
        self.__dict__[self.key] = value


class TypeAssert:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        print('__call__', self, args, kwargs)
        print(inspect.signature(self.cls))
        params = inspect.signature(self.cls).parameters
        print(params)
        for name, param in params.items():
            print(name, '----------------', param, '-------', param.annotation)
            if param.annotation != param.empty:
                setattr(self.cls, name, TypeCheck(name, param.annotation))
        print('+++++++++++++++++++++', self.cls.__dict__)
        return self.cls(*args, **kwargs)


@TypeAssert
class Person:
    def __init__(self, name: str, age: int, hight: int):
        self.name = name
        self.age = age
        self.hight = hight


# 这种方法的
p1 = Person('tom', 123, 123)
print(p1.name, p1.age, p1.hight)
