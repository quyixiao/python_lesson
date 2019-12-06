def gen():
    print('line 1 ')
    yield 1
    print('line 2 ')
    yield  2
    print('line 3 ')
    return 3


next(gen()) #line 1
next(gen()) #line 1
next(gen()) #line 1
g = gen()
print(next(g)) #line 1
print(next(g)) #line 2
#print(next(g)) #line 3
print(next(g,' end '),) #StopIteration: 3



# yield 暂停当前函数执行，让出当前的控制，这个时候，又是一个生成器对象，
# 同一个生成器对象，如果找不到，则直接返回缺省值
# next() 的下一个函数，line 3 只能打印一次，如果有yeild ，表示一个生成器函数，
# 可以用next() 或者 for 来，一个生成器函数中，可以有多个yeild 函数,如果
# 有return 语句，则退出
# next() 可以加一个缺省值，在生成器对象里面，一般，return  和yeild 之前的


# 在生成器函数中，使用多个yeild语句，执行一次会暂停执行，把yield 表达式返回
# 再执行会执行，会到下一个yield语句
# return 语句依然可以终止函数 运行，但是return 语句返回的值不能被获取到
# return 会导致无法继续获取下一个值，抛出stopItermtion异常
# 如果函数没有显示的return 语句，如果生成器函数执行到结尾，一样会抛出StopIterration异常
# 没有多余的，
