# Shape基类，要求所有的子类都必须提供面积计算，子类，三角形，矩形，圆
# 上题圆类的数据可序列化
import math


class Shape:
    def __init__(self):
        pass

    @property
    def area(self):
        raise NotImplementedError("未实现基类")


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def area(self):
        a, b, c = self.a, self.b, self.c
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b


    @property
    def area(self):
        a, b = self.a, self.b

        return

class Circle(Shape):
    pass  # 圆形
