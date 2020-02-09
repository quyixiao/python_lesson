# 浏览器，WSGI Server  WSGI APP
#  Http 请求，解包封装，调用app
# Http状态码，报文头，
# HTTP 正文
#
# WSGI 服务器 wsgiref
# wsgiref 这是一个WSGI参考实现库
#

from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server


def simple_app(environ, start_response):
    setup_testing_defaults(environ)
    status = '200 OK'
    headers = [('Content-Type', 'text/html')]
    start_response(status, headers)
    ret = [("%s:%s\n" % (key, value)).encode('utf-8')
           for key, value in environ.items()]
    print(ret )
    return ret


httpd = make_server('0.0.0.0',8000,simple_app)
print('SErver on port 8000...')
httpd.serve_forever()