# 函数是python 中的一等公民，
# 函数也是对象，可调用的对象
# 函数可以作为普通变量，参数，返回值
# 高阶函数
# 数据概念y = g(f(x))
# 在数学计算科学中，高阶函数应当至少满足下面的一个条件函数
# 接收一个或者多个函数作为一个参数
# 输出一个函数
#

def counter(base):
    def inc(step=1):
        nonlocal base
        base += step
        return base

    return inc


c = counter(10)
c2 = counter(10)

print(c())
print(c())
print(c())
print(c())
print('------------------------------------------------')
print(c == c2)  # 返回的是两个函数
print(c2())
print(c2())
print(c2())
print(c2())



