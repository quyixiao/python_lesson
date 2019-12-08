def add(x, y):
    # Python 文档字符串，Documentation Strings
    # 在函数的语句块的第一行，且习惯多行

    """
    this is add function
    example :
        add(4,5)
    """

    return x + y


# 装饰器的本质，就是对函数功能上的增强，后置增强，装饰器函数，就是我们看到的东西
# 技术就是来源于生活，我们是可以输出到控制台的，

print("name = {} \n doc = {}".format(add.__name__,add.__doc__))
print(help(add))