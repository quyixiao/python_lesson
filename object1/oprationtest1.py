# 运算符重载应用场景
# 往往是用面向对象实现类，需要做大量的运算，而运算符是这种运算在数学上最常见的表达式，例如，上例中的对+进行了运算符重载，实现了
# Point类的二元操作重新定义为 Point+Point
# 提供了运算符重载，
#

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "repr : {} {} {} ".format(id(self), self.x, self.y)

    def __add__(self, other):
        self.x = self.x + other.x
        self.x = self.y + other.y
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __iadd__(self, other):
        return self + other

    def __gt__(self, other):
        return self.x + self.y > other.x + other.y

    def __lt__(self, other):
        return self.x + self.y < other.x + other.y


p1 = Point(4, 4)
p2 = Point(3, 3)

p1 + p2  # 返回类型
p1 += p2

print(p1.x, p1.y)  # 返回类型

p3 = p1 + p2
p1 += p2
print(p1.x, p1.y)
print(p3.x, p3.y)

print('---------------------------------------------------------')
print(p1 > p2)
print(p1 < p2)

print(p1 == p2)


