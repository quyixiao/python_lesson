# 实现 staticMothod 装饰器的，完成 staticmethod 装饰器的功能
# 实现 classmethod 装饰器的，完成 装饰器的功能
from functools import partial


class StaticMethod:
    def __init__(self, fn):
        self.fn = fn

    def __get__(self, instance, owner):
        print('StaticMethod___get__')
        return self.fn  # StaticMethod 类型的对象 s_mtd

    def __call__(self, *args, **kwargs):
        pass


class ClassMethod:
    def __init__(self, fn):
        self.fn = fn

    #
    def __get__(self, instance, owner):
        print('ClassMethod___get__')
        return self.fn(owner)  # StaticMethod 类型的对象 s_mtd


class A:
    #
    @StaticMethod
    def s_mtd():
        print('-------111111-----------')

    #  都可以直接调用
    @ClassMethod
    def c_mtd(cls):
        print(cls)
        print('{} class method ')


A.s_mtd()  # StaticMethod 类型的实例
A.c_mtd  # 可调用，函数，可调用对象
