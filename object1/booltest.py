# __bool__ 内建函数 bool()，或者对象放在逻辑表达式位置，调用这个函数返回布尔值，没有定义__bool__(),
#
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __bool__(self):
        return True


    def __repr__(self):
        return "__repr__<Point x={} ,y={}>".format(self.x, self.y)


    def __str__(self):
        return "<Point {} {} {} >".format(id(self),self.x,self.y)

# 如果自己的类没有，那么就找父类要，
class TriPoint(Point):
    pass

p1 = Point(4,5)
p2 = Point(4,500)

print(dir(p1))
print(bool(p1),bool(p2))

print(bool(TriPoint)) #如果是一个类对象，类对象是一个 bool 函数，所有的对象都是真的，我们现在说的这些东西，是实例的
#

if p1 :
    print('11111111111111111111')


if TriPoint(4,5):
    print('832983988932')


tp = TriPoint(4,5)

print('-------------------------------')
print('repr',repr(p1))
print('str',str(p1))

print('--------------------')
print('repr',repr(tp))
print('str',str(tp))


class B :

    def __repr__(self):
        return " B repr "

print([p1,B()]) # 如果没有写的话，那么直接调用基类的


