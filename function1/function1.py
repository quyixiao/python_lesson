x = 5


def a():
    # x += 1
    print(x)


a()

print(x)

print('------------------------------------------------')


# 找外部要，如果没有的话，外部对内部是可见的，
# 在本地的范围内定义了一个本地变量，外部变量的作用域，外部作用，相当于对这个变量
# 相当于在外部的范围内重新定义了一个o,外部，是自己的，
# 外部
def out2():
    o = 65

    def inner():
        o = 97
        print('inner {}'.format(o))
        print(chr(o))

    inner()
    print('outer {}'.format(o))


out2()

x = 5
def foo():
    y = x + 1

def foo1():
    x = 1
#def foo2(): 在本地的语句块中定义了x ,在本地定义了x,等号的右边定义了x,优先的定义，
#    x += 1

#



