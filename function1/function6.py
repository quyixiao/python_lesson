
def foo(xyz=1): # xyz 这个虽然是局部变量，但是，全局使用域中使用，外部是看不到内部的，但是内部是可以使用外部的
    print(xyz)


foo()
foo()
#print(xyz)