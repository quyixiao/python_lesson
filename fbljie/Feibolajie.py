import sys


def fib(n):
    return 1 if n < 2 else fib(n - 1) + fib(n - 2)


for i in range(0, 20):
    print(fib(i), end=' ')

# 没有递归调用的话
# 递归异常
#
