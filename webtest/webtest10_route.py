import re
from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server, demo_app
from urllib.parse import parse_qs
from webob import Request, Response

from webob.dec import wsgify


# wsgify 装饰器装饰的一个函数应该具有一个参数，这个参数是webob.Request类型，是对字典environ的对象化后的实例
# 返回值
# 可以是一个webob.Response类型的实例
# 可以是一个
# 什么是路由
# 简单的说，就是中怎样的走，就是按照不同的路径分发数据
# URL 代表着不同的资源的地址访问，可以认为请求不同的路径对应的数据，对于动态网页技术来说，不同的路径应该对
# 应不同的应用程序来处理，返回数据, 用户以为还是访问的静态的网页
# 所以代码中要增加对 URL 的处理
# 不管是静态 WEB 服务器，还是动态的 WEB服务器，都需要路径和资源或处理程序的映射，最终返回 HTML的文本
#  静态的 WEB服务器，解决路径和文件之间的映射
# 动态的 WEB服务器解决路径和应用程序之间的映射
#  所有的 WEB 框架都是如此，都有路由配置
# 路由功能的实现
# app 是 WSGI 中的程序，但是，
# match 方法必须从头开始匹配，只匹配一次
# serch 方法，只匹配一次
# fullmatch 方法要完全匹配
# findall 方法，从头开始，找到所有的匹配的列表
# finditer 方法，返回找到所有的匹配的迭代器
# 字典的问题
#  如果使用字典，key保存的是路径，普通的字典遍历
@wsgify
def app(requst: Request) -> Response:
    # return b'<h1>magedu.com</h1>' bytes
    # return Response('9ds98ds9898ds98')
    return '<h3>python.org</h3>'


class Router:
    ROUTERTABLE = []

    @classmethod
    def register(cls, path):
        def wrapper(handler):
            cls.ROUTERTABLE.append((re.compile(path), handler))
            return handler
        return wrapper

@Router.register(r'^/$')
def indexhandler(request: Request):
    return 'indexhandler'

@Router.register(r'^/python$')
def pythonhandler(request: Request):
    return 'pythonhandler'


def donothing(request: Request):
    pass

# Router.register('/',indexhandler)
# Router.register('/python',pythonhandler)
#

class App:
    _Router=Router

    @wsgify
    def __call__(self, request: Request):
        path = request.path
        for pattern,handler in self._Router.ROUTERTABLE:
            matcher = pattern.match(path)
            if matcher:
                return handler(request)
        raise Exception('404')


httpd = make_server('0.0.0.0', 8000, App())

print('SErver on port 8000...')
try:
    httpd.serve_forever()
except:
    httpd.server_close()
