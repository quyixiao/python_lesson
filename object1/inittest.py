#
class A:
    def __init__(self, a, d):
        self.a = a
        self.__d = d

    def showprivate(self):
        print(self.__d)

class B(A):
    def __init__(self, b, c):
        A.__init__(self, b + c, 6)
        self.b = b
        self.c = c

    def printv(self):
        print(self.b, self.c)
        print(self.a)  # 去自己的实例字典中去找，再到 B 中的实例中找，再到 A 中找，A 的类字典中有没有，如果没有直接抛出异常
        #print(self.__d)  # AttributeError: 'B' object has no attribute '_B__d'
        super().showprivate()


# 上例代码中，

b = B(4, 5)
b.printv()
