from functools import total_ordering

# 上面的例子中大大简化了代码，但是一般来说比较实现等于或者小于方法也就够用，其它可以不实现，所以这个装饰器只是看着很美好
# 且可以会带来性能问题，建义需要什么方法，建义
@total_ordering
class A:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return "repr : {} {} ".format(id(self), self.x)

    def __eq__(self, other):
        return self.x == other.x

    def __gt__(self, other):
        return self.x > other.x









