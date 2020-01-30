# 问题的引出
# 都是字典惹出的祸
# 字典为了提升查询效率，必须用空间换时间
# 一般来说一个对象，属性多一点，都存储在字典便于查询，问题不大
# 但是如果数百万的对象，那么字典占用得就比较大了
# 这个时候，能不能把属性字典__dict__省略了
# 规模一旦上去就都是问题，加起来就不是事情了，空间换取时间，
# 空间换取时间，python 就提供了一个特殊的变量，
# 这个问题是一个问题，我们要创建很多的对象
# 上面的两个问题，存入属性的字典，这个是一个
#
class A:



    X = 1
    __slots__ = 'x'

    def __init__(self):
        self.y = 5
        self.z = 6

    def __add__(self, other):
        print('A__add__')

    def __iadd__(self, other):
        print('A__iadd__')





    def show(self):
        print(self.X, self.y, self.z)


class B :
    def __init__(self):
        self.x = 5




a = A()
b = B()
a + b