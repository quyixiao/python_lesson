# 有二十数字，两两配对，关键是如何分析这个
from object1.Randomtst import RandomGenerator1


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point {}:{}>".format(self.x,self.y)


ri = RandomGenerator1()
points = [Point(x, y) for x, y in zip(ri.generator(), ri.generator())]
points = [Point(*v) for v in zip(ri.generator(), ri.generator())]
# print(list(points)) #  如果觉得惰性求值的方式是怎样的 python 是通过自己的字典来实现的

for point in points:
    print(point)












