# 函数
# 函数的定义 y = f(x) ,y 是 x 的函数，x 是自定义变量
# Python  函数
# 由若干语句组成的语句块，函数的名称，参数列表，它是组织代码的最小单元
# 完成一定任务功能
#
#  函数的作用
#  结构你继续说我只对代码的最基本的
#  在 def 语句定义函数
#  def 函数名参数列表
#  函数体（代码块）
#  函数名就是标识符，命名要求也是不一样的
#  语句必须缩进，约定4个空格
#  Python 语句函数没有 return 语句，隐式的返回一个 None 值
#  定义中的参数列表成为形式参数，只是一种符号表答，简称形参
#  调用
#  函数定义 ，只是声明一个函数，它是会被执行，需要调用
#  调用方式，就是函数名加上小括号，括号内写上参数
#  调用时写的参数实际参数，是实实在在的传入值，简称参数
#  有多个变量，在 python 中 没有 return 语句，如果没有将隐式的返回一个 None
#

# 函数举例
# def add (x,y) :
#       result = x + y
#       return result
# out = add(4,5 )
# print(out)
# 上面只是定义了一个函数，有一个函数的名字做add,接收两个参数
# 计算的结果，通过返回值返回
# 调用通过函数名add 加2个参数，返回的值可以使用变量接收
# 定义需要在调用前，也就是调用时，已经定义过了，否则抛出NameError 异常
# 函数的可调用对象 ，callable()
# 看看这个函数是不是通用的，体会一下函数的好处
#


def add(x, y):
    result = x + y
    return result


out = callable(add(4, 5))  # 函数是可调用对象
# 函数调用时传入的参数要和定义的个数相匹配（可变参数例外）
# 位置参数
# def f (x,y,z) 调用使用f (1,3,5)
# 按照参数定义顺序传入参数
# 关键字参数
# def f(x,y,z) ，调用使 f(x=1,y=2,z=3)
# 使用形参数的名字来出入实参的方式，如果使用了形参名字，那么传参的有顺序就可以定义顺序不同
# 传参数
# f(z=None,y=10,x=[1])
# f((1,),z=6,y=4.1) # 一个元组是一个参数，命名的方式来实现，传参数的方式是，将
# f(y=5,z=6,2)
# 要求位置参数必须在关键字参数之前传入，位置参数是按位置对应的
# 使用参数的名字来出入实参的方式，
# out = add(4, 5)
print(out)


def add1(x, y):
    return x + y


# 在定义的时候使用
print(add1(y=9, x=4))
# 我们东西
print(add1(1, y=2))

#  SyntaxError: positional argument follows keyword argument ,位置参数必须放到前面

# print(add(x = 1 ,7))
# print(add(5))  TypeError: add() missing 1 required positional argument: 'y'
# print(add(x = 5 ))
# print(add()) TypeError: add() missing 2 required positional arguments: 'x' and 'y'

# print(add(y = 8 )) # TypeError: add() missing 1 required positional argument: 'x'


# def add2(x = 5 ,y):
#   return x + y
# 作用
# 参数默认值可以在未传入足够的位置参数可以使用关键字传入参数的
# 到目前为止，我们传入的参数都是位置参数
# 参数非常多的时候，并不需要用户每次都输入所有的参数，简化的函数调用
# 只需要将他关注的必须要变的参数传递进来，每次进来的时候，

def add4 (x,y=5):
    return x + y

print(add4(3))
print(add4(x = 5 ))
#print(add4(y = 3 )) TypeError: add4() missing 1 required positional argument: 'x'

# 位置参数定义
def login(host,port,username,password):
    return host










