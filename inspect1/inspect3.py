import functools
import inspect


def check(fn):  # 检查传入的参数是否符合要求
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(fn)
        params = sig.parameters  # 有序字典
        # （4,'abc'） args
        # keys = [x for x in params.keys()]
        # [int,int]
        # (4,'abc') args
        #
        keys = list(params.keys())
        values = list(params.values())
        for i, val in enumerate(args):
            if values[i].annotation is not inspect._empty and isinstance(val, values[i].annotation):
                print(keys[i], '==', val)

        # 关键字参数
        #
        for k, v in kwargs.items():
            if params[k].annotation is not inspect._empty and isinstance(v, params[k].annotation):
                print(k, '=====', v)
        result = fn(*args, **kwargs)
        return result

    return wrapper


@check
def add(x: int, y: int = 7) -> int:
    return x + y


print(add(4, y=3))

print('--------------------------------')
print(add(y=10, x=3))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print(add(10,x = 4 )) #TypeError: add() got multiple values for argument 'x'
# 业务应用
# 有函数如下
# 请检查用户输入的是否符合输入的要求
# 最好让用户感觉不到你加入了东西，非侵入性的，在python 中在大量的装饰器的使用
# 对用户输入的
# 如果业务没有定义注解，
