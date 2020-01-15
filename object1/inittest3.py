# 多继承弊端
# 多继承很好的模似了世界，因为事物很少的单一继承，但是丢弃简单，必然引入复杂性，带来了冲突
# 多继承实现会导致编译器设置的复杂度，所以现在很多的这么认为也舍弃了类的多继承
# java 中的一个类可以实现多个接口，
# 多继承可能会带来二义性，例如，猫和狗都继承自动物，现在如果一个类多继承了猫和狗，在我们的实现中
# Python 使用的 MRO(method resolution order ) 解决基类搜索顺序的问题
# 由于历史原因，MRO 有三个搜索算法
#
class A:
    pass


class B(object):
    pass


print(dir(A))
print(dir(B))
print(A.__bases__)
print(B.__bases__)

# 古典类 在旧式类中，
a = A()
print(a.__class__)
print(type(a))
