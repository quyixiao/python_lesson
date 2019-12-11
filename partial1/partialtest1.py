# 
import functools

functools.partial


def add(x, y):
    return x + y


def partial(func, *args, **keywords):
    def self(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords) #不能影响到原来的方法

    self.func = func  # 对原来的函数的包装<-add
    self.args = args  # 空元组
    self.keywords = keywords
    return self  # 返回一个新的函数

newadd = partial(add, y=6)  # newadd = newfunc
print(newadd(4))  # newadd(4) x=4 y = 8 (1,1) add





