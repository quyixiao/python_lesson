import time
import datetime
from functools import wraps, update_wrapper


def timeit(output=lambda fn, delta: print("timeit : {} took {} s ".format(fn.__name__, delta))):
    def _timeit(fn):
        @wraps(fn) # wrapper = wraps(fn)(wrapper)
        def wrapper(*args, **kwargs):
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            delta = (datetime.datetime.now() - start).total_seconds()
            output(fn, delta)
            return ret

        return wrapper

    return _timeit


@timeit()
def add1(x, y):
    time.sleep(2)
    return x + y


def add(x, y):
    """This is a add function """
    time.sleep(2)
    return x + y

# add(4, 5)
# 每个地方不同的类型 这个类可以当成一个函数使用，那么，我们就可以将他当成一个函数
class TimeIt:
    def __init__(self, fn, output=lambda fn, delta: print("timeit : {} took {} s ".format(fn.__name__, delta))):
        self._fn = fn
        self.output = output
        print('__init__')

    def __enter__(self):
        print('__enter__')
        self.start = datetime.datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        delta = (datetime.datetime.now() - self.start).total_seconds()
        self.output(self._fn, delta)

    def __call__(self, *args, **kwargs):
        print('__exit__')
        return self._fn(args[0], args[1])


with TimeIt(add) as obj:
    print('pre')
    print(obj._fn(5, 6))
    time.sleep(3)
    print('end ')
