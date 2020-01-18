# Descriptors
# 描述器的实现
# 用到三个魔术方法，__get__(),__set__(),__delete__()
# object.get__(self.instance,owner)
# object.__set__
# 这个类，我们称为描述器
# 一步步的引导他们，描述器，a,b 两个类，在 a 中实现了 get,set 方法，而这个类属性

class A:
    def __init__(self, x):
        print('A__init__',x)
        self.x = x

    def __set__(self, instance, value):
        print('A__set__',self, instance, value)

    def __get__(self, instance, owner):
        print('A__get__',self, instance, owner)

    def __del__(self):
        pass

class B :
    print('B__instance ')
    x = A(2)  # 类的实例，一定是一个实例
    print('-------------',x )

    def __init__(self):
        print('B__init__')
        self.x = A(3)
        print('+++++++++++++++==',self.x)

a = A(1)
print(a.x)
a.x = 220
print(a.x)
print('|'*100)
b = B()
print('*'*100)
print(b.x )
b.x = A(456)
print('/'*100)
print(B.x)



