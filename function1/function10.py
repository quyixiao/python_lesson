def foo(xyz=[],u='abc',z = 123):
    xyz = xyz[:]
    xyz.append(1)
    print(xyz)
    return xyz

foo()
print(foo.__defaults__)
foo()
print(foo.__defaults__)
foo([10])
print(foo.__defaults__)
print('----------------',foo([10,20]))
print(foo.__defaults__)


# 如果想修改原来参数，来实现这个问题，
#

