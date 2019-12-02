# 函数的作用
# 结构化编程的对代码的最基本的封装，一般功能组织一段代码
# 调用
# 参数
# 函数体
# 在python 我觉得这这是一个东西，如果
# 位置参数在相应的位置上用缺省的值来代替
#
def add(*nums):
    sum = 0
    for x in nums:
        sum += x
    print(sum)


add(3, 6, 9)


def showconfig(**kwargs):
    for k, v in kwargs.items():
        print('{} = {}'.format(k, v))


# 形参数

showconfig(host='127.0.01', port='8080', username='zhangsna', password='123455')


# def showconfig1(username,password,**keyarges)


def fn(x, y, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)


fn(3, 5, 7, 9, 10, a=1, b='python')
print('--------------------------------------')
fn(3, 5)
print('=============================================')
fn(3, 5, 7)
print('++++++++++++++++++++++++++++++++++++++++++++')
fn(3, 5, a=1, b='python')
print('|||||||||||||||||||||||||||||||||||||||||||||')


# fn(7,9,y=5,3=7,a=1,b='python') # 错误，7 和 9分别赋给


def fn(*args, x):
    print(x)
    print(args)


def fn1(x=5, **kwargs):
    print(x)
    print(kwargs)


fn1()
fn1(x=5)
print('--------------------------')
fn1(5)

fn1(x=5, y=6)

print('-------------------------------')
fn1(y=6, x=5)

print('--------------------------------')
fn1(3, y=10)


# fn1(y = 10,3 )

# 参数列表一般顺序是，普通参数，缺省参数，可变位置参数，keyword-only参数（可缺省值）可变关键字参数
def fn2(x, y, z=3, *args, m=4, n, **kwargs):
    print(x, y, z, m, n)
    print(args)
    print(kwargs)


# fn2() TypeError: fn2() missing 2 required positional arguments: 'x' and 'y'
fn2(1, 2, n=4)  # 这样还真的可以的


#

# fn(1,2,10,11,x=7,n=5) ypeError: fn() got an unexpected keyword argument 'n'
# fn(1,2,10,n=5) #TypeError: fn() got an unexpected keyword argument 'n'

# fn(1,2,10,2,n=5,t = 10)TypeError: fn() got an unexpected keyword argument 'n'

def connect(host='localhost', port='3306', user='admin', password='zhangsan', **keyargs):
    print(keyargs)


connect(db='cmdb')
connect(host='172.19832.', db='cmdb')
connect(host='192,16.1.123', db='cmdb')


def add(x, y):
    return x + y


add(4, 5)
# add((4,5))
t = (4, 5)
# add[t[0],t[1]] #TypeError: 'function' object is not subscriptable
add(t[0], t[1])
add(*t)
add(*(4, 5))
add(*range(1, 3))
add(*[4, 5])
add(*{4, 6})


def add5(x, y):
    print(x, y)
    return x + y


add5(*(4, 5))

add(*[4, 5])

print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;')
d = {'x': 5, 'y': 6}
add5(**d)
# 将一个对象给解了
add5(*d.keys())
# add(**{'a':5,'b':6}) TypeError: add() got an unexpected keyword argument 'a'
add5(*d.values())


# add5(**{'a':5,'b':6})TypeError: add5() got an unexpected keyword argument 'a'


def add6(*iterrable):
    result = 0
    for x in iterrable:
        result += x
    return result


add6(1, 2, 3)
add6(*[1, 2, 3])
add6(*range(10))


# 返回的是一个tuple的值
def fn(a, b):
    return a, b

# 如果编写一个函数
print(type(fn(4, 5)))


# 编写一个函数，能接受两个参数，返回最大值和最小值
# 编写一个函数，接受一个参数n,n 为正整数，左右两个参数打印方式，要求数据必须对齐
#

