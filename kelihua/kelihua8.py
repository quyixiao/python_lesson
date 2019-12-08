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


def copy_properties(src, dest):
    dest.__name__ = src.__name__
    dest.__doc__ = src.__doc__
    # ... 还有很多的属性，用这种方式，还是可以解决很多的名字变量，这些属性是感觉都没有变化过

# 在使用装饰器的时候，出现一个问题，就是原来的属性被顶掉了，使用这些属性，标识符和名称是俩码事，
# 标识符，是用来作变量的，和内存作变量的
# 名称，是用来给我们程序猿看的
# 标识符，只是用来看的，但是，warraper 的属性，我们学习，标识符是哪一样东西，
#
def logger(fn):
    def wrapper(*args, **kwargs):
        """ I am wrapper """
        print('args={},kwargs={}'.format(args, kwargs))
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        duration = datetime.datetime.now() - start
        print('function {} take {} s  '.format(fn.__name__, duration.total_seconds()))
        return ret

    copy_properties(fn, wrapper)
    return wrapper


@logger
def add(x, y):
    """
    this is add function
    """
    print('-------------------------------------')

    sleep(2)
    return x + y


print(add(4, 5), add.__name__, add.__doc__)
