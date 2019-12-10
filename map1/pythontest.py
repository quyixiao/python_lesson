# Python 是动态语言，变量随时可以赋值，且能赋值为不同的类型
# Python 不是静态编译型语言，变量类型是在运行时决定的
# 动态语言很灵活，但是也在这种特性的
#
#
def add(x,y):
    """
    :param x:int
    :param y:int
    :return:int
    """
    return x + y

print(add(4,5 ))
print(add('hello ','world '))
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
add(4,'hello')
# 难发现，由于不做任何类型，
# 难使用，函数的使用者看到函数的时候，并不知道你的函数的设计，并不知道应该传入什么类型
# 函数改变了，但是文档没有更新，如果文档没有更新，但是代码改变了，所以最好是阅读源码，对于数学而言
#






















