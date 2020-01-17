def a():
    print(' function a ')


# 函数即对象，对象 foo()
a.__call__()


#
# print(dir(a))
# print(callable(a))
# #print(isinstance(a, Callable))
#
#
# class A:
#     def __call__(self, *args, **kwargs):
#         print(args)
#         print(kwargs)
# print('----------------------------------')
# print(callable(A))
# print(callable(A()))
# #print(callable(1,3,5,x=6,z=7))
# A()(1,3,5,x=6,z=7)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, *args, **kwargs):
        return "<Point {}:{}>".format(self.x, self.y)


p = Point(4, 5)
print(p)
print(p())

#  练习
# 定义一个斐波那契列的类，方便调用，计算第 n 项
class Adder:
    def __init__(self):
        self.sum = 0

    def __call__(self, *args, **kwargs):
        for x in args:
            self.sum += x

        return self


a = Adder()
print(a(1, 2, 3, 4, 5, 6, 7, 8, 9).sum)
