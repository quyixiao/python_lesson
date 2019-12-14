# 实现一个 cache装饰器，实现可以过期被清除的功能
# 简化设置，函数的形参定义不包含可变位置参数，可变关键词参数和 keyword-only 参数
# 可以不考虑缓存存满之后的换出问题
# 数据类型的选择
#  缓存应用场景，是有数据要频繁的查询 ，且每次计算要大量的计算或者等待时间之后才能返回结果的情况，
# 使用缓存 提高查询的速度，用空间来换时间
# key 的存储
# 中 key 必须是 hashtable
# key 能接受的位置
# lru_cache 实现了第一种，可以看出单独的处理了位置参数和关键字参数
# key 的要求,key 必须是 hashable
#  由于 key 是所，但是如果 key有不可的 hash 类型数据，就无法完成
# lru_cache 就不可以了
# 缓存是必须使用 key,但是 key 必须是可hash的，所以只能适用实参是不可变类型的函数调用
# key 算法的实现，
# inspect 模块获取函数签名之后，取 paramters，这是一个有序的字典，会保存所有的参数信息
# 装饰器是 AOP面向对象切面编程的思想，Aspect Oriented Programming 的思想的体现
# 面向对象往往需要通过继承或者组合依赖等方式调用一些功能，这些功能的代码住住可能在多个类中实现
# 例如 logger ,这样造成代码的重复，增加了耦合，logger 改变影响所有的使用他的类或者方法
# 而 AOP需要的类或者方法上切下，前后的切入点可以增强，调用和被调用都被解耦
# 这是一种不修改原来的代码的业务代码，给程序动态添加功能和技术，例如 logger 函数功能就是对业务函数增加日志
#  而业务代码应该和日志功能剥离干净
#  装饰器的应用场景
#  日志，监控，权限，设计，参数检查 ，路由的处理
# 这些功能与业务无关，很多的业务都需要公共的功能，所有的适合独立出来的，需要的时候，对目标进行对象增强
# 这些往往是一种公共的功能，在 java 中用来对我们日志的增强
#


# 如果没有完成
import inspect
from collections import OrderedDict
from datetime import datetime


def cache(fn):
    local_cache = {}  # 缓存key () 元组 ，value 返回值

    def _wapper(*args, **kwargs):
        def make_key(fn):
            # make_key
            key = tuple()
            sig = inspect.signature(fn)
            params = sig.parameters  # 这里面的所有的 key 都在存在的
            keys = list(params.keys())
            # add(4,5,z=6) add(4,y=5,z=6)
            params_dict = OrderedDict()
            # 位置参数
            for i, val in enumerate(args):
                k = keys[i]
                params_dict[k] = val  # {'x':4 ,'y':5}

            # 关键字参数
            for k, v in sorted(kwargs.items()):
                params_dict[k] = v

            # 使用缺省值
            for k, param in params.items():
                if k not in params_dict.keys():
                    params_dict[k] = param.default;

            key = tuple(sorted(params_dict.items()))
            print('key========',key)
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
