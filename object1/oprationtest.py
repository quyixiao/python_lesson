# 运算符重载
# operator  模块提供了下的特殊方法，可以将类的实例使用下面的操作符来操作
# < , <= ,== , > , >= ,!=   特殊方法 __lt__ ,__le__,
# +,-,*,/,%,//,**,divmod        __add__,__sub__,__mul__,__truediv__,__mod__,__floordiv__,__pow__,__divmod__
# +=,-=,*=,/=,%=,//=,

class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def __sub__(self, other):
        return self.age - other.age

    def __isub__(self, other):  # -=
        print('-=')
        # return Person(self.name, self.age - other.age)
        return Person(self.name, self.age - other.age)


print('-----------------------sub-----------------')
tom = Person('tom')
jerry = Person('jerry', age=16)
print(tom - jerry)
print(tom.__sub__(jerry))
print(jerry - tom)
print(jerry.__sub__(tom))
print('-----------------------__isub__-----------------')
jerry -= tom
print(jerry.age)








