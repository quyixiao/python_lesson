# 如果没有完成
# 实现一个 cache 装饰器，实现可过期的被清除的功能
# 简化设计，函数的形参不包含可变位置参数，可变关键词参数和 keyword-参数
# 上面的4种，可以下面的两咱理解
# lru_cache 实现了一种，可以单独的处理的位置参数和关键字参数
#  但是函数的定义 def add(4,y=5) ，使用了默认值，如何理解add(4,5) 和 add(4)是否一样呢？
#  如果认为一样，那么 lur_cache 无能为力
# 1,2,3,4 全部相同
# 缓存必须使用 key,但是 key 必须是可 hash 的，所以只能适用实参是不可变类型的函数调用
# key 算法设计
# 这两种方式是不是排序的，如果没有实现，自己实现的缓存，也是在人家的前提出，
# 日志装饰器，查看代的执行的时间
#
import inspect
from collections import OrderedDict
from datetime import datetime


def cache(fn):
    local_cache = {}  # 缓存key () 元组 ，value 返回值

    def _wapper(*args, **kwargs):
        def make_key(fn):
            """生成字典的 key"""

            # make_key
            sig = inspect.signature(fn)
            params = sig.parameters  # 这里面的所有的 key 都在存在的
            print('params', params)
            keys = list(params.keys())
            # add(4,5,z=6) add(4,y=5,z=6)
            params_dict = OrderedDict()
            # 位置参数
            for i, val in enumerate(args):
                k = keys[i]
                params_dict[k] = val  # {'x':4 ,'y':5}
            #
            # # 关键字参数
            # for k, v in sorted(kwargs.items()):
            #     params_dict[k] = v

            # 使用缺省值
            for k, param in params.items():  # 所以的定义了参数
                if k not in params_dict.keys():
                    if k in kwargs.keys():  # 你提供了
                        params_dict[k] = kwargs[k]
                    else:
                        params_dict[k] = param.default
            key = tuple(sorted(params_dict.items()))
            print('key========', key)
            return key

        key = make_key(fn)
        # 查询和缓存的问题
        if key not in local_cache:
            local_cache[key] = fn(*args, **kwargs)
        return local_cache[key]

    return _wapper


def logger(fn):
    def wapper(*args, **kwargs):
        start = datetime.now()
        ret = fn(*args, **kwargs);
        print(fn.__name__, (datetime.now() - start))
        return ret

    return wapper


@cache
@logger
def add(x, y=5, z=6):
    return x + y + z


print(add(4, 5, z=6))
print(add(4, 5))
print(add(4, y=5))

print(add(x=4, z=6, y=5))
