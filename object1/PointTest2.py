# 这种动态的修改一个属性的方法和装饰器修饰一个类，差别是什么呢？
# 这些东西他们之前的差异是什么，如果
# 动态的属性修改，是定义是，类定义，继承是在定义的时候就写死了
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "{}:{}".format(self.x, self.y)

    def show(self):
        print(self.x, self.y)


p = Point(4, 5)
print(p)

setattr(p, 'z', 100)
setattr(p, 'y', 100)
print(p)
setattr(Point, 'x', 200)
print(p)
print(getattr(p, "__dict__"))
print(getattr(Point, "__dict__"))
p.show()
print('--------------------------------------------')
setattr(Point, 'show', lambda self: print(self.x + self.y))
p.show()

print('|||||||||||||||||||||||||||||||||||||')
setattr(p,'show',lambda self : print( self.x ,'-------------' ,self.y))
# 实例上是可以放方法定义
# 我们用自己正常的方法定义
p.show(p)
#
print( hasattr(p,'x'))