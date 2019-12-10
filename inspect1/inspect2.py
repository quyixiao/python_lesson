import inspect


def add(x, y: int = 7, *args, z, t=10, **kwargs) -> int:
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
print('params', sig.parameters)
print('return :', sig.return_annotation)
print('~~~~~~~~~~~~~~~~~~~~~')
for i, item in enumerate(sig.parameters.items()):
    name, param = item
    print(i + 1, name, param.annotation, param.kind, param.default)
    print(param.default is param.empty, end='\n\n')
