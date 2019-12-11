import functools
import inspect


def add(x,y,* args) -> int:
    print(args)
    return x + y

newadd = functools.partial(add,1,3,6,5)
print(newadd(7))
print(newadd(7,10))
#print(newadd(9,10,y=20,x = 26))
print(newadd())


print(inspect.signature(newadd))