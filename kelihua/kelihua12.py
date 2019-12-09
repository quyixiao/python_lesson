import datetime
import functools
from time import sleep

# 这个将下面的参数，

def logger():  # #logger(5) == _logger add=_logger
    def _logger(fn):
        # @_inner == wrapper == _inner(wrapper)
        def wrapper(*args, **kwargs):
            """ I am wrapper """
            print('args={},kwargs={}'.format(args, kwargs))
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            duration = datetime.datetime.now() - start
            print('function {} take {} s  '.format(fn.__name__, duration.total_seconds()))
            return ret
        #
        functools.update_wrapper(wrapper, fn)
        return wrapper

    return _logger



def logger1():  # #logger(5) == _logger add=_logger
    def _logger(fn):
        # @_inner == wrapper == _inner(wrapper)
        @functools.wraps(fn) # wrapper = functools.wraps(wrapper)(fn)
        def wrapper(*args, **kwargs):
            """ I am wrapper """
            print('args={},kwargs={}'.format(args, kwargs))
            start = datetime.datetime.now()
            print(id(wrapper))
            ret = fn(*args, **kwargs)
            print(id(wrapper))
            duration = datetime.datetime.now() - start
            print('function {} take {} s  '.format(fn.__name__, duration.total_seconds()))
            return ret
        return wrapper

    return _logger



# 现在，可以将函数写得非常的灵活了
@logger()  # add = logger(add)
def add(x, y):
    """
    this is add function
    """
    print('-------------------------------------')
    sleep(2)
    return x + y


print(add(4, 5), add.__name__, add.__doc__,add.__wrapped__)
