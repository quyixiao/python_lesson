#
#
import inspect


def add(x: int, y: int, *args, **kwargs) -> int:
    """
    :param x: 对于单一的数据类型，收集不同类型的数据
    :param y:
    :param args: 对于可变参数，没有必要加限制，也不支持加
    :param kwargs:
    :return:
    """
    return x + y


sig = inspect.signature(add)
print(sig)
params = sig.parameters;
print(sig.parameters)  # 这个必须是要有顺序的，如果没有顺序的话，没法实现，参数定义，annotation，位置拿出来的时候，返回的就是一个有顺序的

print(sig, type(sig))  # 这个
print(params['x'])
