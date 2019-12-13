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
