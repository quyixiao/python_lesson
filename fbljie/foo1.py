import sys


def foo1():
    foo1()


# foo1() # RecursionError: maximum recursion depth exceeded
# 当出现一定情况
print(sys.getrecursionlimit())  # 一个进程中的内存空间是有限制的，用递归，一定要小心，如果执行不到，if 1 return
# 如果if 没有写好的话，还是有性能问题的
#
