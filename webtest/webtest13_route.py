import re
from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server, demo_app
from urllib.parse import parse_qs
from webob import Request, Response

from webob.dec import wsgify

# 构架处理流程
# 客户端发来的 HTTP请求，被 WSGI服务器处理后传递给 APP的__call__。
# App 中遍历已经注册的 Routers,Routers 的 match 来判断是不是自己已经处理了，前缀匹配，就看注册的规则，当然 规则
# 被装饰器已经转换了成了命名分组的正则表达式了
#  如果由某一个注册的正则表达式匹配，就把获取的参数放到 request 中，并调用注册时映射的 handler 给它传入 request
# handler 处理后，返回的 response  ，App中拿到这个 response 的数据，返回给最初的 wsgi
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


class Router:
    def __init__(self, prefix: str = ''):
        self.__prefix = prefix.rstrip('/\\')  # 前缀，例如/product
        self.__routetable = []  # 存在三元组，装饰器

    def route(cls, pattern, *methods):
        def wrapper(handler):
            cls.ROUTERTABLE.append(
                (tuple(map(lambda x: x.upper(), methods)),
                 re.compile(pattern), handler))
            return handler

        return wrapper

    @classmethod
    def get(cls, pattern):
        return cls.route(pattern, 'GET')

    @classmethod
    def POST(cls, pattern):
        return cls.route(pattern, 'POST')

    @classmethod
    def head(cls, pattern):
        return cls.route(pattern, 'HEAD')

    def match(self, request: Request):
        # 必须先匹配前缀
        if not request.path.startswith(self.__prefix):
            return None
        # 前缀匹配，说明就必须这个 Router 实例独步一时，后续匹配不上，依然返回 None
        for methods, pattern, handler in self.__routetable:
            # not methods 表示一个方法都没有定义，就是支持全部方法
            if not methods or request.method.upper() in methods:
                # 前提已经是以__prefix开头了，可以 replace，去掉 prefix 剩下的才是正则表达式需要匹配的路径
                matcher = pattern.match(request.path.replace(self.__prefix, '', 1))
                if matcher:  # 正则匹配
                    # 动态为 request 增加属性
                    request.groups = matcher.groups()  # 所有的分组组成的元组，包括命名分组
                    request.groupdict = AttrDict(matcher.groupdict())  # 命名分组组成的字典
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


# 创建 Router 对象
idx = Router()
py = Router('/python')
# 注册
App.register(idx, py)


@idx.get(r'^/$')
@idx.route(r'^/(?P<id>\d+)$')  # 支持所有的方法访问
def indexhandler(request: Request):
    print(request.groups)
    print(request.groupdict)
    return 'indexhandler'


@Router.get('^/(\w+)$')
def pythonhandler(request: Request):
    res = Response()
    res.charset = 'utf-8'
    res.body = 'welcom to ma python'.encode()
    return res


if __name__ == '__main__':
    httpd = make_server('0.0.0.0', 8000, App())
    print('SErver on port 8000...')
    try:
        httpd.serve_forever()
    except:
        httpd.server_close()
