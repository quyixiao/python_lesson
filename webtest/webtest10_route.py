from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server, demo_app
from urllib.parse import parse_qs
from webob import Request, Response

from webob.dec import wsgify


# wsgify 装饰器装饰的一个函数应该具有一个参数，这个参数是webob.Request类型，是对字典environ的对象化后的实例
# 返回值
# 可以是一个webob.Response类型的实例
# 可以是一个
@wsgify
def app(requst: Request) -> Response:
    # return b'<h1>magedu.com</h1>' bytes
    # return Response('9ds98ds9898ds98')
    return '<h3>python.org</h3>'


class Router:
    ROUTERTABLE = {}

    @classmethod
    def register(cls, path):
        def wrapper(handler):
            cls.ROUTERTABLE[path] = handler
            return handler
        return wrapper

@Router.register('/')
def indexhandler(request: Request):
    return 'indexhandler'

@Router.register('/python')
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
        try:
            return self._Router.ROUTERTABLE.get(path)(request)
        except:
            raise Exception('404')


httpd = make_server('0.0.0.0', 8000, App())

print('SErver on port 8000...')
try:
    httpd.serve_forever()
except:
    httpd.server_close()
