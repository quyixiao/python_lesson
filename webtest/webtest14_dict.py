#  字典属性化
# dict 有没有效
#
import re


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

# str  不包含/的任意字符，默认类型               [^/]+
# word 字母和数字                                \w+
# int   纯粹数字，正负数                        [+-]?\d+
# float     正负号，数字，包含               [+-]?\d+.\d+
# any       包含/的任意字符            .+
#  类型设计，支持 str,word ,int,float,any 类型
# 还可以考虑一种 raw类型，
# 问题，
# 目前路由匹配使用正则表达式定义，不友好，很多的用户不会以使用正则表达式，能否简化
# 分析
# 生产环境，URL是规范，不能随便书写，路径是很有意义的，尤其是对 restful 风格
# 所以，要对 URL规范
#  例如/product/1110892398，这就是一种规范，也是规范了，背后的故事是什么
#



# '/{id:int} #=> '^/(?P<id>\d+)$'
TYPEPATTERNS = {
    'str': r'[^/]+',
    'word': r'\w+',
    'int': r'[+-]?\d+',
    'float': r'[+-]?\d+\.\d+',
    'any': r'.+'
}
name = 'id'
t = 'int'
print('/(?P<{}>){}'.format(name,TYPEPATTERNS.get(t,TYPEPATTERNS['str'])))

print('*'*100)
src = '/student/{name}/{id:int}/{age:int}'

#pattern = r'/{([^{}:]*):([^{}:]*)}'
pattern = r'/{([^{}:]+):?([^{}:]*)}'
regex = re.compile(pattern)
matcher = regex.search(src)
print(matcher)
print(matcher.groups())
def repl(matcher):
    name = matcher.group(1)
    t = matcher.group(2)
    return '/(?P<{}>){}'.format(name,TYPEPATTERNS.get(t,TYPEPATTERNS['str']))


#print(regex.sub(repl,src))
print('-----------')

def parse(src:str):
    start = 0
    res = ''
    for matcher in regex.finditer(src):
        print(matcher)
        res += src[start:matcher.start()]
        name = matcher.group(1)
        t = matcher.group(2)
        tmp = '/(?P<{}>){}'.format(name, TYPEPATTERNS.get(t, TYPEPATTERNS['str']))
        res += tmp
        start = matcher.end()
    else:
        res += src[start:]
    return res

print(parse(src))


