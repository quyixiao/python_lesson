# 描述器 Descripttors
# 用到了3个魔术方法: __get__(),__set__(),__delete_ 三个方法中的任何一个，
#  数据只有 get 的话，就是数据器
#  非数据描述符，non-data-descriptor
# 同时出现了__get__，

class A:
    def __init__(self,x):
        self.x = x
        print('A__init__')
    def __set__(self, instance, value):
        print(3,'A__set__',self,instance,value)
        return instance


    def __get__(self, instance, owner):
        print(4,'A__get__',self,instance,owner)
        return instance


class B:
    x = A(1111)
    def __init__(self):
        print('B___init__')
        self.a1 = 'b1'

print(5,B.x)
b = B()
print(6,b.x)
print(7,b.a1 )
print(b.__dict__)
print('-------------------------------')
b.x= 100
print(b.x)

print(b.__dict__)



print('*'*100)

class D :
    x = [1,2,3]
    def __init__(self):
        self._y = 5

    @classmethod
    def show(self):
        pass

    show = 1
    @property
    def y(self):
        return self._y


d = D()
d.x = 100
print(d.__dict__)

print(D.__dict__)
d._y = 500


d.show = 2
print(D.__dict__)

D.show = 123

print(D.__dict__)

#d.y = 2  # AttributeError: can't set attribute
d._y = 2
