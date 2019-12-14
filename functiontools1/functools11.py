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
# 一般缓存系统都在过期的功能
# 它是某一个 key 过期，可以对每一个 key 单独设置过期的时间，也可以对这些 key 统一的设定过期时间
# 缓存的时候，它是某一个 key过期，可以对第一个 key 单独的过期时间，也可以对这些 key 统一的设定的时间过期
# 可以解决服务器的并发压力有很大的好处，不向数据库，真的用起来的时候，各是个的东西，缓存
# 别以人这些都是运维做的事情，进程内的缓存，是要过期的，过期有几种办法，
# 过期，为每一个 key 设置单独的过期的时长，
# 我们这一次实现还是简单一点的
# 每一个 key 可以设置一个过期的时长
# 当 key 的生成，多钱程的问题
# 资源争用的问题
# 当 key生存超过这个时间，就会被自动清除，注意，这里并没有考虑多线程问题，而且这种过期的机制，每一次都遍历所以的数据
# 大量的数据的时候，遍历可能效率有一定的问题
# 在上面的装饰器增加一个参数，需要用到了这个参数装饰器了
# @mag_cache(5) 代表 key 生成5称后过期
# 带参数装饰在原来的装饰器外面的嵌套一层
# 清除的时机，何时清除呢？清除过期的 key ?
# 缓存中设定的时候，又要设定时间，又要设定时长
# 一个线程钢表不除过期的 key 这个以后实现，本次创建的 key  之前，清除所有的过期的 key
# 过期的时间
# 元组的实现
# 编程中要考虑的问题，写的时候，还是要注意对内存的消耗
# 如果有能力，就将我们写的东西实现
#

import inspect
from collections import OrderedDict
from datetime import datetime
import time

def cache(t):
    def _cache(fn):
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
            print('------------t-------------',t )
            key = make_key(fn)
            # 查询和缓存的问题
            if key not in local_cache:
                ret = fn(*args, **kwargs)
                print('333333333333333333',ret)
                a = tuple([ret,(time.time() + t * 1000)])
                print(a )
                local_cache[key] = a
                return ret
            else:
                print('++++++++++++++++++++++++++++++++')
                a = local_cache[key]
                if True :
                    ret = fn(*args, **kwargs)
                    print('44444444444', ret)
                    a = tuple([ret, (time.time() + t * 1000)])
                    print(a)
                    local_cache[key] = a
                    return ret
                return a[0]

        return _wapper
    return _cache



def logger(fn):
    def wapper(*args, **kwargs):
        start = datetime.now()
        ret = fn(*args, **kwargs);
        print(fn.__name__, (datetime.now() - start))
        return ret

    return wapper


@cache(5)
@logger
def add(x, y=5, z=6):
    return x + y + z


print(add(4, 5, z=6))
print(add(4, 5))
print(add(4, y=5))

print(add(x=4, z=6, y=5))
