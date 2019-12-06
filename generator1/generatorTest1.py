# 生成器对象generator
# 生成器指的是生成器对象，可以由生成器表达式来得到，也可以使用yield关键字得到一个生成器
# 调用函数来得到这个生成器对象
# 生成器函数
# 函数体中包含了yield语句的函数，返回生成器对象
# 生成器对象，是一个可迭代对象，是一个可迭代对象
# 生成器对象，是可延迟计算的，惰性求值
#


def inc():
    for i in range(5):
        yield i


print(type(inc))
print(type(inc()))
x = inc()       # <class 'function'>
print(x)        # <class 'generator'>
print(type(x))  # <generator object inc at 0x10ca941d0>
print(next(x))  # <class 'generator'>

for m in x:
    print(m, '*')

print('---------------------------------')
for m in x: # 这个时候，是一个空集合，一定是一个迭代器，这个是一个可迭代对象，生成器函数，返回值是很特别的。
    print(m, '**')

#


#print(next(x)) #StopIteration