print((lambda x: x * 2)(4))
foo = lambda x, y: (x + y) ** 2
print(foo(2, 1))
# 使用lambda 关键字来定义匿名函数
# 参数列表不需要小括号的
# 冒号是用来分割参数列表和表达式
# 使用lambda 只能写在一行上，被称为单行函数
#
# 用途
# 在高阶函数传参时，使用lambda表达式，往往能简化代码
#


print((lambda: 0)())
print((lambda x, y=3: x + y)(5))
print((lambda x, y=3: x + y)(5, 6))
print((lambda x, *, y=30: x + y)(5))
print((lambda x, *, y=30: x + y)(5, y=10))
print((lambda *args: (x for x in args))(*range(5)))
print((lambda *args: [x + 1 for x in args])(*range(5)))
print((lambda *args: {x + 2 for x in args})(*range(5)))

print([x for x in (lambda *args: map(lambda x: x + 1, args))(*range(5))])

print([x for x in (lambda *args: map(lambda x: (x + 1, args), args))(*range(5))])
