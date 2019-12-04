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
lst = foo(lst)
print(lst)
print(5,foo.__defaults__)
# 默认值的作用域
# 每一种方式
# 使用影子拷贝创建一个新的对象 ，永远不能改变传入的参数
# 第二种方式
# 通过值的判断就可以灵活的选择，
# 这种方法灵活，应用广泛
# 很多的函数的定义，都可以看到，如果传入的是非null,那么惯用的用法，
# 使用nonlocal关键字，将变量标记为在上级的局部的作用域中定义，但是不能是全局的作用域中定义，
# 属性_defaults_

