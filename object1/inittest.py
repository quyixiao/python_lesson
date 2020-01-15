class A:
    def __init__(self, a):
        self.a = a


class B(A):
    def __init__(self, b, c):
        A.__init__(self, b + c)
        self.b = b
        self.c = c



    def printv(self):
        print(self.b, self.c)
        print(self.a)  # 去自己的实例字典中去找，再到 B 中的实例中找，再到 A 中找，A 的类字典中有没有，如果没有直接抛出异常


b = B(4, 5)
b.printv()
