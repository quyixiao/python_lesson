
def foo(xyz=[]): # 局部变量都是引用类型
    xyz.append(100)
    print(xyz)


foo()
foo()
foo()
foo()
# print(xyz)
