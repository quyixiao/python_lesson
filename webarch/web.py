import re
from wsgiref.simple_server import make_server, demo_app
from webob import Request, Response
from webob.dec import wsgify
from webarch.myutils.AttrDict import AttrDict
from webarch.template import render


class Router:
    # '/{id:int} #=> '^/(?P<id>\d+)$'
    TYPEPATTERNS = {
        'str': r'[^/]+',
        'word': r'\w+',
        'int': r'[+-]?\d+',
        'float': r'[+-]?\d+\.\d+',
        'any': r'.+'
    }

    TYPECAST = {
        'str': str,
        'word': str,
        'int': int,
        'float': float,
        'any': str
    }

    _regex = re.compile(r'/{([^{}:]+):?([^{}:]*)}')

    def __init__(self, prefix: str = ''):
        self.__prefix = prefix.rstrip('/\\')  # 前缀，例如/product
        self.__routetable = []  # 存在三元组，装饰器

    def _repl(self, matcher):
        name = matcher.group(1)
        t = matcher.group(2)
        return '/(?P<{}>{})'.format(name, self.TYPEPATTERNS.get(t, self.TYPEPATTERNS['str']))

    def parse_back(self, rule):
        return self._regex.sub(self._repl, rule)

    def parse(self, src: str):
        start = 0
        res = ''
        types = {}  # 字典
        for matcher in self._regex.finditer(src):
            print(matcher)
            res += src[start:matcher.start()]
            name = matcher.group(1)
            t = matcher.group(2)
            types[name] = self.TYPECAST.get(t, str)  # 获取数据类型
            tmp = '/(?P<{}>{})'.format(name, self.TYPEPATTERNS.get(t, self.TYPEPATTERNS['str']))
            res += tmp
            start = matcher.end()
        else:
            res += src[start:]
        return res, types

    def route(self, rule, *methods):
        def wrapper(handler):
            pattern, types = self.parse(rule)
            self.__routetable.append(
                (tuple(map(lambda x: x.upper(), methods)),
                 re.compile(pattern),
                 types,
                 handler)
            )
            return handler

        return wrapper

    def get(self, pattern):
        return self.route(pattern, 'GET')

    def POST(self, pattern):
        return self.route(pattern, 'POST')

    def head(self, pattern):
        return self.route(pattern, 'HEAD')

    def match(self, request: Request):
        # 必须先匹配前缀
        if not request.path.startswith(self.__prefix):
            return None
        # 前缀匹配，说明就必须这个 Router 实例独步一时，后续匹配不上，依然返回 None
        for methods, pattern, types, handler in self.__routetable:
            print(methods, pattern, types, handler)
            # not methods 表示一个方法都没有定义，就是支持全部方法
            if not methods or request.method.upper() in methods:
                # 前提已经是以__prefix开头了，可以 replace，去掉 prefix 剩下的才是正则表达式需要匹配的路径
                noprefix = request.path.replace(self.__prefix, '', 1)
                matcher = pattern.match(noprefix)
                if matcher:  # 正则匹配
                    # 动态为 request 增加属性
                    request.groups = matcher.groups()  # 所有的分组组成的元组，包括命名分组
                    # 解决类型问题
                    newdict = {}
                    for k, v in matcher.groupdict().items():
                        newdict[k] = types[k](v)
                    request.groupdict = AttrDict(newdict)  # 命名分组组成的字典
                    return handler(request)


class App:
    _ROUTERS = []  # 存储所有的一级 Router 对象

    # 注册
    @classmethod
    def register(cls, *routers: Router):
        for router in routers:
            cls._ROUTERS.append(router)

    @wsgify
    def __call__(self, request: Request):
        # 遍历_ROUTERS,调用Router 实例的 match 方法，看谁匹配，
        for router in self._ROUTERS:
            response = router.match(request)
            if response:  # 匹配返回的非 None 的 Router 对象
                return response  # 匹配则立即返回

        raise Exception('404')

