import time
import datetime
from functools import wraps, update_wrapper

# 每个地方不同的类型 这个类可以当成一个函数使用，那么，我们就可以将他当成一个函数
# 怎样写代码，是不是要初始化函数来实现，文档字符串来实现
# 上下文应用场景
# 增强功能
# 在代码执行前后增加代码，以增强其功能，类似装饰器的功能
# 资源管理
# 打开了资源需要关闭，例如文件对象，网络连接，数据库连接等
# 权限管理
# 在执行代码之前，做权限的验证，有 __enter__中处理
# 退出之前一定能做到资源清理
# 锁，都用上下文管理
#
class TimeIt:
    """Time It class """
    def __init__(self, fn, output=lambda fn, delta: print("timeit : {} took {} s ".format(fn.__name__, delta))):
        self._fn = fn
        self.output = output
        print('__init__')
        self.start = datetime.datetime.now()
        #self.__doc__ = fn.__doc__
        #update_wrapper(self,fn)
        wraps(fn)(self) # 拷备doc

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')

    def __call__(self, *args, **kwargs):
        ret = self._fn(args[0], args[1])
        delta = (datetime.datetime.now() - self.start).total_seconds()
        self.output(self._fn, delta)
        print('__call__')
        return ret


@TimeIt
def add(x, y):
    """This is a add function """
    time.sleep(2)
    return x + y


print(add(4,5))
print(add.__doc__)