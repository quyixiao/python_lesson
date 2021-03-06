# 一个加法函数，想增强化的函数功能，能够输出被调用的参数信息
# def add(x,y)
# return x + y
# 增加信息的输出功能
# def add(x,y):
# def print(call add ,x + y )# 日志输出到控制台
# return x + y
# 上面的函数是完成了需求，但是以下的缺点是
# 打印语句的耦合太高
# 加法的函数属于业务，能输出信息的功能，属于非法业务功能代码 ，不该入在业务函数加法中
# 在一个函数调用的前面和后面打印这些参数，如果这些，如果有这么一些函数，我们能不能不用

def logger(fn):
    def wrapper(*args, **kwargs):
        print('before', *args)
        ret = fn(*args, **kwargs)
        print('end ', ret)
        return ret

    return wrapper


@logger
def add1(x, y, *, z=6):  # add1 = logger(add1)
    return x + y + z


@logger
def add(x, y):
    return x + y


# 我们看看能不能正常的执行，
add1(4, 5, z=7)  # logger(add1,4,5,z = 7 )
add(4, 5)


# 装饰器
# 无参原装饰器，@logger ，他是一个函数，他的返回值，函数作为形参，
# 这个返回值也是一个参数，返回值也是一个函数
# 不同的函数，返回一个@functionname 来被用这个语法糖，装饰器一定是一个高阶函数
# 装饰器只是对函数的功能，只是对原有的函数进行功能的增强，

