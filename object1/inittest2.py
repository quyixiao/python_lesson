# B 的实例初始化过程是不会调用父类的init方法的，如果调用到了，那就这样子
# 如果说父类中有 init，子类中一般是想用父类的东西，函数的调用，一般是你你想要什么就什么，父类中的身高和体重
# Python  不同版本的类
# Python2.2 之前类没有共同的祖先，之后，引入object类，它是所有的类的共同的祖先类object
# Python2中为了兼容，分为古典类，和新式类
# Python3 中的全部是新的式类
#
class A:
    def __init__(self):
        self.a1 = 'a1'
        self.__a2 = 'a2'
        print('A init')


class B(A):
    def __init__(self):
        A.__init__(self)
        self.b1 = 'b1'
        print('B init')


# 上例代码中
b = B()