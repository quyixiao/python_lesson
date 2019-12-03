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


def foo2():  # 在本地的语句块中定义了x ,在本地定义了x,等号的右边定义了x,优先的定义，
    x = 2
    x += 1


#
# 本地的作用域，相同

#
# def foo5 ():
#     global  z #NameError: name 'z' is not defined
#     z = z + 1
#
# foo5()


def foo5():
    global z  # z 是一个全局的变量，
    z = 20
    print(z)
    z = z + 1


foo5()
print(z)


# global 总结
# x += 1 这种特殊的形式产生的错误的原因，先引用后，赋值，而python 动态语言是赋值才有意义的
# 才能被引用，解决办法，在这条语句的前增加x = 0 的赋值语句，或者使用global 告诉内部作用域
# 使用全局的作用域，去全局的用作用域找变量赋值
# global 的使用原则
# 外部的使用域的变量内部的使用域是可见的，但是也不要在这内部的情况使用域直接使用，因为函数的目的就是为了封装
# 尽量与外界隔离
# 如果函数需要使用，
# 闭包
# 自由变量：未在本地作用域使用定义变量，例如定义在内层函数的外层函数的使用域的中的变量
# 闭包是一个概念，出现嵌套函数中，指的是内层函数的引用到外层函数的的自由变量，就形成了闭包，很多的语言都有这个概念，最熟悉的就是JavaScript
# 先看看右边的一段代码
# 第4行的


def counter():
    c = [0]  # 对c中的变量的值进行改变，但是不是对c变量本身进行改变

    def inc():
        c[0] += 1  #
        return c[0]

    return inc


foo = counter()
print(type(foo))  # <class 'int'>
# print(type(foo())) #<class 'function'>
# 元组的是不可以改变的。
print(callable(foo)) # True 这个返回的是True,
print(foo(), foo())  # TypeError: 'int' object is not callable
c = 100  # 这个值通过它的调用，是没有用的，这个值被保留下来了，
print(foo())  # 函数执行完成以后，这个局部变量，外部函数调用，c[] 随着函数的调用，没有结束，这个c表示的是自由变量，使用c[0] 就生成了闭包
# 内部函数使用外部函数的自由变量，就产生了闭包，当前，并没有使用global,
# inc() 这种方式是不可见的
#