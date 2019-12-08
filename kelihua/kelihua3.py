# 一个加法函数，想增强化的函数功能，能够输出被调用的参数信息
# def add(x,y)
# return x + y
# 增加信息的输出功能
# def add(x,y):
# def print(call add ,x + y )# 日志输出到控制台
# return x + y
# 上面的函数是完成了需求，但是以下的缺点是
# 打印语句的耦合太高
# 加法的函数属于业务，能输出信息的功能，属于非法业务功能代码 ，不该入在业务函数加法中
# 在一个函数调用的前面和后面打印这些参数，如果这些，如果有这么一些函数，我们能不能不用

def add(x, y):
    return x + y


def add1(x, y, *, z=6):
    return x + y + z


def logger(fn, *args, **kwargs):
    print('before', args)
    print('before', *args)
    ret = fn(*args, **kwargs)
    print('end ', ret)
    return ret


logger(add, 4, 5)
logger(add1, 4, 5, z=7)
