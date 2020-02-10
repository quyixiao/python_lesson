import re
from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server, demo_app
from urllib.parse import parse_qs
from webob import Request, Response

from webob.dec import wsgify


@wsgify
def app(requst: Request) -> Response:
    # return b'<h1>magedu.com</h1>' bytes
    # return Response('9ds98ds9898ds98')
    return '<h3>python.org</h3>'


class Router:
    ROUTERTABLE = []

    @classmethod
    def register(cls, method: str, path):
        def wrapper(handler):
            cls.ROUTERTABLE.append((method.upper(), re.compile(path), handler))
            return handler

        return wrapper


@Router.register('GET', r'^/$')
def indexhandler(request: Request):
    return 'indexhandler'


@Router.register('GET', r'^/python/(?P<id>\d+)$')
def pythonhandler(request: Request):
    print('----------------id =', request.groupdict.get('id'))
    return 'pythonhandler'


def donothing(request: Request):
    pass


class App:
    _Router = Router

    @wsgify
    def __call__(self, request: Request):
        path = request.path
        for method, pattern, handler in self._Router.ROUTERTABLE:
            if not method == request.method.upper():
                continue
            matcher = pattern.match(path)
            print('method=',request.method.upper())
            if matcher:
                print(matcher.groups())
                print(matcher.group(0))
                print(matcher.group(1))
                print(22222, matcher.groupdict())
                request.groups = matcher.groups()
                request.groupdict = matcher.groupdict()
                return handler(request)


httpd = make_server('0.0.0.0', 8000, App())

print('SErver on port 8000...')
try:
    httpd.serve_forever()
except:
    httpd.server_close()
