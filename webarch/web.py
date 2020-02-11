import re
from wsgiref.simple_server import make_server, demo_app
from webob import Request, Response
from webob.dec import wsgify
from webob.exc import HTTPNotFound,HTTPForbidden

from webarch.myutils.AttrDict import AttrDict
from webarch.template import render
# 根据影响面分为
# 全局拦截
# 在app中的拦截
# 拦截可以是多个，多个拦截器执行是有顺序的
# 数据response前执行的命名preinterceptro，之后为postinterceptor
# 大多数都是合适的，拦截器做数据转换，合法的html数据，对于
# request ，用response的某些数据
# 加入拦截器功能的方式
# 1.app和Router类直接加入
# 把拦截器的相关方法，属性分别添加到相关的类中
# 实现简单
# 2.Mixin
# App和Router类直接拦截
# App JSON的支持，拦截器位置不同，对某个拦截器进行拦截，
# 拦截点的不同，拦截面的不同
# 在Router 中拦截
# 权限拦截
# 如果用户没有登陆的话，直接跳转到登陆页面，打开一个handler ，request 中，如何
# 全局，有的时候是全局的，有的时候是部分的，前缀
# 拦截器可以是多个，
# 拦截器是允许还是不鸡的，做的都是这些事情，拦截器在框架中经常看见的这些问题
# 怎样组织，怎样才能合理，这样的东西是一个项目吗？
# 总结   1. 熟悉WSGI的编程接口
#           2.强化模块化，类封装的思想
# 3.增强分析业务能力
# 这个构架基本具备了WSGI的框架基本功能，其他的框架都类似
# 权限验证，SQL注入检测的功能使用拦截器实现
#
#
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
        self.__pre_interceptor__ = []
        self.__post_interceptor__ = []


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
        for fn in self.__pre_interceptor__ :
            request = fn(request)
            if request is None:
                return None

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
                    response =  handler(request)
                    for fn in self.__post_interceptor__:
                        response = fn(request,response)
                    return response


class App:
    _ROUTERS = []  # 存储所有的一级 Router 对象
    # 全局拦截器
    PRE_INTERCEPTOR = []  # 拦截器函数
    POST_INTERCEPTOR = []  #

    # 注册
    @classmethod
    def register(cls, *routers: Router):
        for router in routers:
            cls._ROUTERS.append(router)

    @wsgify
    def __call__(self, request: Request):  # 路由，url调试入口
        # 拦截
        for fn in self.PRE_INTERCEPTOR:
            request = fn(request)
            if not request:
                raise HTTPForbidden('没有页面')
        # 遍历_ROUTERS,调用Router 实例的 match 方法，看谁匹配，
        for router in self._ROUTERS:
            response = router.match(request)
            if response:  # 匹配返回的非 None 的 Router 对
                for fn in self.POST_INTERCEPTOR:
                    response = fn(request, response)
                return response  # 匹配则立即返回

        raise Exception('404')


# IP过滤
# 全局IP过滤
def ip_filter(request: Request):
    prefix = '127.'
    print(request.remote_addr)
    return request if request.remote_addr.startswith(prefix) else None