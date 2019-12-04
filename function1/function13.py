def foo(xyz=[], u='abc', z=123):
    xyz.append(1)

    def inner(a=10):
        pass
    print(inner)       # 两个函数不一样 <function foo.<locals>.inner at 0x106556710>

    def inner(a=100):
        print(xyz)

    print(inner) # 两个函数不一样<function foo.<locals>.inner at 0x1064f68c0>
    return inner


bar = foo()
print(id(foo), id(bar), foo.__defaults__, bar.__defaults__)
del bar
print(id(foo), foo.__defaults__)
print(id(foo), id(bar), foo.__defaults__, bar.__defaults__) #NameError: name 'bar' is not defined




