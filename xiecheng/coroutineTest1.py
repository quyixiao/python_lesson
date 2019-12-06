# 协程
# 生成器的高级用法
# 是用户空间调试函数的一种实现
# Python3 asyncio 就是协程实现，已经加入到标准库
# Python3.5 使用async,await 关键字直接原生支持协程
# 协程调试器的实现思路
# 有2个生成器A,B
# next(A)后，A执行


def inc():
    for x in range(100):
        yield  x

foo =  inc()
print(next(foo))
print(next(foo))
print(next(foo))