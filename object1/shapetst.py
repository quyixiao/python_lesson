# Shape基类，要求所有的子类都必须提供面积计算，子类，三角形，矩形，圆
# 上题圆类的数据可序列化
import math
import json
import msgpack
import pickle


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
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width, self.height


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        return self.r * self.r * 0.25 * math.pi


class SerializableMxin:
    def dumps(self, m='json'):
        if m == 'json':
            return json.dumps(self.__dict__)
        elif m == 'msgpack':
            return msgpack.dumps(self.__dict__)
        else:
            return pickle.dumps(self.__dict__)


class SerializableCircleMxin(SerializableMxin, Circle): pass

d = SerializableCircleMxin(4)
print(d.area)



