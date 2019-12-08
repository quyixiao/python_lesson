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
import datetime
from time import sleep


def logger(fn):
    def wrapper(*args, **kwargs):
        print('args={},kwargs={}'.format(args, kwargs))
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        duration = datetime.datetime.now() - start
        print('function {} take {} s  '.format(fn.__name__, duration.total_seconds()))
        return ret

    return wrapper


@logger
def add(x, y):
    # Python 文档字符串，Documentation Strings
    # 在函数的语句块的第一行，且习惯多行
    """
    this is add function
    """

    sleep(2)
    return x + y


add(4, 5)
# 装饰器的本质，就是对函数功能上的增强，后置增强，装饰器函数，就是我们看到的东西
# 技术就是来源于生活，我们是可以输出到控制台的，