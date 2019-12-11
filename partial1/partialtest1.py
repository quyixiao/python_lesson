# 
import functools

functools.partial


def add(x,y):
    return x + y

def partial(func, *args, **keywords):
    def self(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)

    self.func = func
    self.args = args
    self.keywords = keywords
    return self

newadd = partial(add,y = 6 )
print(newadd(4 ))
