#  字典属性化
# dict 有没有效
#
class AttrDict:
    def __init__(self, d: dict):
        self.__dict__.update(d)

    def __setattr__(self, key, value):
        raise NotImplementedError()

    def __repr__(self):
        return "{}".format(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

d = {'a': 100, 'b': 200}
obj = AttrDict(d)
print(obj.a)
print(obj.b)

obj.__dict__['a'] = 2000
print(obj.a)
