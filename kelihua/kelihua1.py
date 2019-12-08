# 柯里化
# 指的是将原来的参数，

def add(x, y):
    return x + y


def add(x):
    def _fn(y):
        return x + y

    return _fn


t = add(4)(5)
print(t)
# 通过嵌套函数就可以把函数转换成柯里化函数
#




