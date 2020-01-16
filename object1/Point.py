#
from pandas._libs import json

class A:
    def __init__(self,name):
        self.name = name

    def __bytes__(self):
        return json.dumps(self.__dict__).encode()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "__repr__<Point x={} ,y={}>".format(self.x, self.y)

    def __hash__(self):
        return hash((self.x + self.y))

    def __eq__(self, other):
        return self.x + self.y == other.x + other.y

    def __str__(self):
        return "__str__<Point x={} ,y={}>".format(self.x, self.y)

    def __bytes__(self):
        return json.dumps(self.__dict__).encode()

# print(hash(Point(4, 5)))
#  如果一个类不能被 hash ，就将 __hash__设置成 hash  算法就好了

lst = [Point(1, 2), Point(3, 4)]
print(lst)

dic = {Point(1, 2), Point(1, 2)}
print(dic)

p1 = Point(1, 2)
p2 = Point(1, 3)
print(p1 == p2)

print(dir(p1))
print(hash(p1))
print(bytes(p1))




print('str:a,1')

s = '1'
print(s)

print(['a'],(s,))
print({s,'a'})



print(bytes(A('tom')))




