# 把一个函数扁平化
source = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': {'g': 4}}}


# 这个容器由你来提供
# recursion
# 能不能不暴露外界的字典给你呢？字典在内部创建的，在大函数之内，由内部实现了呢？
#
def flatmap(src, target=None, prefix=''):
    if target is None:
        target = {}
    for k, v in src.items():
        if isinstance(v, (list, tuple, set, dict)):
            flatmap(v, target, prefix=prefix + k + '.')  # 递归调用
        else:
            target[prefix + k] = v
    return target


print(source)
print(flatmap(source))
