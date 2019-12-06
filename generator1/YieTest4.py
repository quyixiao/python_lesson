# lambda表达式是匿名了函数
# return 返回的是一个匿名的函数
# 等价于下面的代码
#
def fib():
    x = 1
    y = 2
    while True:
        yield y
        x, y = y, x + y


foo = fib()
for _ in range(5):
    print(next(foo))

for _ in range(100):
    next(foo)
print(next(foo))

