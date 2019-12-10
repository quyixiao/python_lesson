# 函数注解 function Annotation
# 函数的注解，不是强制性要求的，如果非要强制性的用其他的，后果自负
# 这种提示也是友好性的，如果你非不这样写，那也没有办法，程序还是允许运行的，参数注解
#
# 函数注解
# Python 3.5 引入
# 对函数的参数进行类型注解
# 对函数的返回值进行类型注解
# 对于函数参数做一个辅助性的作用,提供给第三方，做代码分析，发现隐藏的bug
# 函数注解，annotation
#
#
def add(x: int, y: int) -> int:
    """
    :param x:
    :param y:
    :return:
    """
    return x + y


print(help(add))
print(add(4, 5))
print(add('mag', 'edu'))
print(add.__annotations__['x'])  # {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}
print(add.__annotations__)
#  <class 'int'> 这个是一个类类型，
print(type(add.__annotations__['x']))  # 这个是一个类类型，允许类型改变，但是类型还在存在的
print(isinstance(add.__annotations__['x'], int))  #
#

i: int = 6
print(i)  #
# 思路
# 函数应该作为参数检查
# 检查函数是一种侵入性的，公用的东西
# 能做能用的检查
# __annotation__是一个字典，是没有顺序的，所以，无法实现
# inspect 模块
# 提供获取
#
#