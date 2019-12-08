import datetime
from time import sleep


def copy_properties(src):
    def inner(dest):
        dest.__name__ = src.__name__
        dest.__doc__ = src.__doc__
        return dest

    return inner

def logger(exet): # #logger(5) == _logger add=_logger
    def _logger(fn):
        @copy_properties(fn)  # wrapper = wrapper copy_properties(fn)(wrapper)
        # @_inner == wrapper == _inner(wrapper)
        def wrapper(*args, **kwargs):
            """ I am wrapper """
            print('args={},kwargs={}'.format(args, kwargs))
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            duration = datetime.datetime.now() - start
            if duration.total_seconds() > exet:
                print('function {} take {} s  '.format(fn.__name__, duration.total_seconds()))
            return ret
        return wrapper
    return _logger

@logger(5)      # add = logger(add)
def add(x, y):
    """
    this is add function
    """
    print('-------------------------------------')

    sleep(2)
    return x + y


print(add(4, 5), add.__name__, add.__doc__)
