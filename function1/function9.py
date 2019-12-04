# 属性_default_中使用元组保存所有的默认值，
def foo(w ,u = 'abc',z = 123):

    u  = 'xyz'
    z = 789
    print(w,u,z)
print(foo.__defaults__)
foo('mage')
print(foo.__defaults__)

#默认值的作用域
# 可变类型默认值，如果使用默认值，就可能修改这个默认值
