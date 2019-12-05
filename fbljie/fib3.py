pre = 0
cur = 1
print(cur, end=' ')


def fib(n, pre=0, cur=1):
    pre, cur = cur, pre + cur
    print(cur, end=' ')
    if n == 2:
        return
    fib(n - 1, pre, cur)


fib(10)
