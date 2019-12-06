def gen():
    print('line 1 ')
    yield 1
    print('line 2 ')
    yield  2
    print('line 3 ')
    yield 3


next(gen()) #line 1
next(gen()) #line 1
next(gen()) #line 1
g = gen()
print(next(g)) #line 1
print(next(g)) #line 2
print(next(g)) #line 3
print(next(g),' end ') #StopIteration: 3



# yield 暂停当前函数执行，让出当前的控制，这个时候，又是一个生成器对象，
# 同一个生成器对象，
