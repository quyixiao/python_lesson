# 实现一个 cache装饰器，实现可以过期被清除的功能
# 简化设置，函数的形参定义不包含可变位置参数，可变关键词参数和 keyword-only 参数
# 可以不考虑缓存存满之后的换出问题
# 数据类型的选择
#  缓存应用场景，是有数据要频繁的查询 ，且每次计算要大量的计算或者等待时间之后才能返回结果的情况，
# 使用缓存 提高查询的速度，用空间来换时间
# key 的存储
#中 key 必须是 hashtable
# key 能接受的位置
# lru_cache 实现了第一种，可以看出单独的处理了位置参数和关键字参数
# key 的要求,key 必须是 hashable
#  由于 key 是所，但是如果 key有不可的 hash 类型数据，就无法完成
# lru_cache 就不可以了
# 缓存是必须使用 key,但是 key 必须是可hash的，所以只能适用实参是不可变类型的函数调用
# key 算法的实现，
# inspect 模块获取函数签名之后，取 paramters，这是一个有序的字典，会保存所有的参数信息
#



# 如果没有完成
import inspect


def cache(fn):
    local_cache = {}  # 缓存key () 元组 ，value 返回值

    def _wapper(*args, **kwargs):
        # make_key
        key = tuple()
        sig = inspect.signature(fn)
        params = sig.parameters
        keys = params.keys()
        # add(4,5,z=6) add(4,y=5,z=6)
        values = params.values()
        params_dict = {}

        for i, val in enumerate(args):
            key += keys[i], val  # (x,4,y,5,z,6)

        for item in sorted(kwargs.items()):
            key += item

        # 查询和缓存的问题
        if key not in local_cache:
            local_cache[key] = fn(*args, **kwargs)
        return local_cache[key]

    return _wapper


@cache
def add(x, y = 5 , z=6):
    return x + y + z



print(add(4, 5, z=6))
print(add(4, 5))
print(add(4,y = 5 ))

print(add(x=4, z=6, y=5))
