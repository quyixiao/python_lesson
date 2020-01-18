from contextlib import contextmanager
from datetime import datetime

# 用到的时候再说，我其实是不想写这些东西，这个是比较，将代码分开出去，对装饰器有一定的了解
# 我们将这个分离一下
#
@contextmanager
def a(x, y):
    start = datetime.now()
    try:
        yield x + y
    finally:
        exe = datetime.now() - start
        print(exe)


with a(4, 5) as f:
    print(f)

    print('mid')
