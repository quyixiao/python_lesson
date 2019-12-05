import sys


def fib(n):
    return 1 if n < 2 else fib(n - 1) + fib(n - 2)


for i in range(0, 20):
    print(fib(i), end=' ')

# 没有递归调用的话
# 递归异常
#
# 递归函数的效率太低了，我们只能获得最外层的调用，最外层的那一层。
# 每一次都是效率是比较低的，大概的算了一下，基本上，从3 往下算，递归是有深度限制的，如果递归，能不能用递归实现
#