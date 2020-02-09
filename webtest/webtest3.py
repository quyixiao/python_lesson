# 浏览器，WSGI Server  WSGI APP
#  Http 请求，解包封装，调用app
# Http状态码，报文头，
# HTTP 正文
#
# WSGI 服务器 wsgiref
# wsgiref 这是一个WSGI参考实现库
#

from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server,demo_app

server = make_server('0.0.0.0',9000,demo_app)
server.serve_forever()