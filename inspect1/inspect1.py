#
#
import inspect
inspect.Signature

#def add(x: int, y: int, *args, **kwargs,z:int) -> int: 是错误的
def add(x: int, y: int, *args,z:int ,**kwargs) -> int:
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
print(params['y'].annotation)
print(params['args'])
#print(params['*args'])
print(params['kwargs'])
print(params['kwargs'].annotation) #表示这个模块下的空值
print(params['z'])
#Parameter对象
# 保存在元组中的，只是只读的
# name ，参数名字
# annotation ，参数注解，可能没有定义
# default,参数缺省值，可能没有定义
# empty: 特殊类，用来标记default属性或者注释annotation属性的空值
# kind : 实参如何绑定形参，
# POSITIONAL_NOLY,值必须是位置参数提供
# POSITIONAL_OR_KEYWORD 值可以作为关键字或者位置参数提供
# VAR_POSITIONAL ,可变位置参数，对应的*args
# KEYWORD_ONLY ，对应的是*args，后面出现的非可变性参数
# 没有下划线的，
# 全部大写表示这个变量是一个常量
#