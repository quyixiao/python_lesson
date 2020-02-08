class ModelMeta(type):  # 元类
    def __new__(cls, *args, **kwargs):
        print('------------------------------')
        print(cls)
        print(args)
        print(kwargs)
        print('----------------------------')
        return super().__new__(cls, *args, **kwargs)


class A(ModelMeta):
    pass


print(type(A))


class B(metaclass=ModelMeta):
    pass


print(type(B))


class C(B):
    pass

print('============================')

print(type(C))

print('+++++++++')
D = ModelMeta('D',(),{})
print(type(D))