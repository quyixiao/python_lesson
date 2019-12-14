# 把一个函数扁平化
source = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': {'g': 4}}}


# 这个容器由你来提供
# recursion
# 能不能不暴露外界的字典给你呢？字典在内部创建的，在大函数之内，由内部实现了呢？
#
def flatmap(src):
    target = {}

    def _flatmap(src, prefix=''):
        for k, v in src.items():
            if isinstance(v, (list, tuple, set, dict)):
                _flatmap(v, prefix=prefix + k + '.')  # 递归调用
            else:
                target[prefix + k] = v
        return target

    _flatmap(src)
    return target


print(source)
print(flatmap(source))
