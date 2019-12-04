def foo(xyz=[], u='abc', z=123):
    xyz.append(1)
    return xyz


print(foo(), id(foo), foo.__defaults__)


def foo(xyz=[], u='abc', z=123):
    xyz.append(1)
    return xyz


print(foo(), id(foo), foo.__defaults__)
del foo

print(foo(), id(foo), foo.__defaults__)  # NameError: name 'foo' is not defined
# 只要是同名，参数直接覆盖，


