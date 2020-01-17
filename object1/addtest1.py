import time
import datetime
from functools import wraps, update_wrapper

# 每个地方不同的类型 这个类可以当成一个函数使用，那么，我们就可以将他当成一个函数
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