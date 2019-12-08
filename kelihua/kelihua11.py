import datetime
from time import sleep


def copy_properties(src):
    def inner(dest):
        dest.__name__ = src.__name__
        dest.__doc__ = src.__doc__
        return dest

    return inner


def logger(exet, func=None):  # #logger(5) == _logger add=_logger
    def _logger(fn):
        @copy_properties(fn)  # wrapper = wrapper copy_properties(fn)(wrapper)
        # @_inner == wrapper == _inner(wrapper)
        def wrapper(*args, **kwargs):
            """ I am wrapper """
            print('args={},kwargs={}'.format(args, kwargs))
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            duration = datetime.datetime.now() - start
            if duration.total_seconds() < exet:
                func(*args, **kwargs)
            print('function {} take {} s  '.format(fn.__name__, duration.total_seconds()))
            return ret

        return wrapper

    return _logger


def logger1(exet, func=lambda x, y: print(x, y)):  # #logger(5) == _logger add=_logger
    def _logger(fn):
        @copy_properties(fn)  # wrapper = wrapper copy_properties(fn)(wrapper)
        # @_inner == wrapper == _inner(wrapper)
        def wrapper(*args, **kwargs):
            """ I am wrapper """
            print('args={},kwargs={}'.format(args, kwargs))
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            duration = datetime.datetime.now() - start
            if duration.total_seconds() < exet:
                func(*args, **kwargs)
            print('function {} take {} s  '.format(fn.__name__, duration.total_seconds()))
            return ret

        return wrapper

    return _logger






def logger2(exet = 5 , func=lambda x, y: print(x, y)):  # #logger(5) == _logger add=_logger
    def _logger(fn):
        @copy_properties(fn)  # wrapper = wrapper copy_properties(fn)(wrapper)
        # @_inner == wrapper == _inner(wrapper)
        def wrapper(*args, **kwargs):
            """ I am wrapper """
            print('args={},kwargs={}'.format(args, kwargs))
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            duration = datetime.datetime.now() - start
            if duration.total_seconds() < exet:
                func(*args, **kwargs)
            print('function {} take {} s  '.format(fn.__name__, duration.total_seconds()))
            return ret

        return wrapper

    return _logger

def func(x, y):
    print(x, y)


# 现在，可以将函数写得非常的灵活了
@logger1(5, func)  # add = logger(add)
def add(x, y):
    """
    this is add function
    """
    print('-------------------------------------')
    sleep(2)
    return x + y


# 现在，可以将函数写得非常的灵活了
@logger2()  # add = logger(add)
def add1(x, y):
    """
    this is add function
    """
    print('-------------------------------------')
    sleep(2)
    return x + y


print(add(4, 5), add.__name__, add.__doc__)

print('++++++++++++++++++++++')
print(add1(4, 5), add.__name__, add.__doc__)
