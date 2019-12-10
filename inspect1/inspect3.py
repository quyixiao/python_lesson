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
            if isinstance(val, values[i].annotation):
                print(keys[i], '==', val)

        # 关键字参数
        #
        for k, v in kwargs.items():
            if isinstance(v, params[k].annotation):
                print(k, '=====', v)
        result = fn(*args, **kwargs)
        return result

    return wrapper


@check
def add(x: int, y: int = 7) -> int:
    return x + y


print(add(4, y=3))

