# 描述器 Descripttors
# 用到了3个魔术方法: __get__(),__set__()

class A:
    def __init__(self,x):
        self.x = x
        print('A__init__')
    def __set__(self, instance, value):
        print(3,self,instance,value)

    def __get__(self, instance, owner):
        print(4,self,instance,owner)


class B:
    x = A(1111)
    def __init__(self):
        print('B___init__')


print(5,B.x)
b = B()
print(6,b.x)





