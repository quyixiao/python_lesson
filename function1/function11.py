def foo(xyz=None,u = 'abc',z = 123):
    if xyz is None:
        xyz = []
    xyz.append(1)
    print(xyz)
    return xyz

foo()
print(1,foo.__defaults__)
foo()
print(2,foo.__defaults__)
foo([10])
print(3,foo.__defaults__)
foo([10,5])
print(4,foo.__defaults__)


lst = [5]
foo(lst)
print(lst)
print(5,foo.__defaults__)