def foo(xyz=[],m=5,n=6):
    xyz.append(1)
    return xyz

print(1,foo.__defaults__)

print(foo(),id(foo()))
print(2,foo.__defaults__)
print(foo(),id(foo))
print(3,foo.__defaults__)

# 函数的地址并没有变，就是说函数这个对象没有变，调用它，它的属性_defaults_ 中使用元组保存所有的默认值
#