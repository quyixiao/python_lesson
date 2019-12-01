print((i for i in range(5)))  # <generator object <genexpr> at 0x10d8c71d0> 生成器对象表达式

print([i for i in range(5)])  # [0, 1, 2, 3, 4] 生成一个列表

g = (i for i in range(5))

print(g)

for iii in g:
    print(iii)

# () 这个是你找要一个，我就生成一个，如果你不找我要，那么，我也不再生成一个对象
# () 生成器表达式，生成器表达式，生成器对象，range()返回一个对象，如果要元素，就生成一个，[] 即使你不要，我也生成这个对象
# () 这个东西名字叫做惰性求值，
# 语法
# (返回值 for 元素 in 可迭代对象中 if 条件)
# 列表解析式的中括号换成小括号就行了
# 返回一个生成器
# 和列表解析式的区别
# 生成器表达式
# 如果我们知道这个这个东西，如果立即返回一个对象，惰性求值，立即计算，什么时候用。
# python 惰性求值，很多的函数都是惰性的，如果我要用的时候，才进行计算，如果计算量不是很多的，什么时候需要的，就什么时候提前使用，
# 生成器
#


print('===============================')

g = (i ** 0.5 for i in range(5))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# 和列表解析式的对比
# 计算方式，
# 生成器表达式延迟计算，列表解析式立即计算
# 列表解构式需要占用的内存


print((x,) for x in range(10))
#
print({x,(x,[1])} for x in range(10))


