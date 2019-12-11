# functools.update_wrapper(wrapper,wrapped,assigned=WRAing)
#
# partial 方法
# partial 返回的函数是一个偏函数，把一个函数的部分
import inspect
from functools import partial


def add(x, y, z):
    return x + y + z


newadd = partial(add, y=5)  # return new function  返回一个关键字传参数
print(inspect.signature(newadd))
# print(help(newadd))
print(newadd(4, z=5)) # 一个偏函数就可以搞定
