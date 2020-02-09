# 浏览器，WSGI Server  WSGI APP
#  Http 请求，解包封装，调用app
# Http状态码，报文头，
# HTTP 正文
#
# WSGI 服务器 wsgiref
# wsgiref 这是一个WSGI参考实现库
# 名称                含义
# REQUEST_METHON    请求方法,GET,POST
# WSGI APP 应用程序端
# environ和start_response这两个参数可以是任意的合法名，但是一般默认这2个名字
# 应用程序端还是有些其他的规定，暂时不用关系别人怎样的
# 名称，含义
# REUEST_METHON     请求方法,GET,POST等
# PATH_INFO
# envion和start_response 这两个参数名可以是任何合法名，但是一般默认的都是2个名字
# 应用程序端还有其他的规定，暂时不用关心
# environ
# QUERY_SRRING
# start_response
# 它是一个可调用对象，有3个参数，定义如下
# start_response （status,response_headers,exc_info_None）
# status是状态码，例如200OK
# response_headers是一个元素为二元组的列表，例如['content-type','text/plain;charset=utf-8']
# exc_info 在错误的处理时候使用
# start_response应该在返回可迭代的对象之前调用，这个就是返回的报文的正文部分，start_response
# 向外提交正文之前就需要提交定义，
# def application(environ,start_response):
# pass
# class Application:
# def __init__(self,environ,start_response):
# pass
# def __init__
# 服务器
# simple_server 只是参考 用，不能用于生产
# curl -I http://192.168.142.1:9999:/xxx?id=5
# curl -X POST http://192.168.142.1:9999:/yyy -d '{"x":2}'
# -I 使用Header 方法
# -X 指定方法，-d传输数据
# 到这里完成了一个简单的WEB程序开发
# 本质上就是一个TCP服务器，监听在特定的端口上
# 支持HTTP协义，能够将HTTP请求报文进行解析，能够把响应数据进行HTTP协义的报文封装并返回浏览器端
# 实现了WSG协义，访协义约定了和应用程序之间的接口，
# 应用程序
# APP应用程序
# 新人WSGI协义
# 本身是一个可调用的对象
# 调用start_response，返回响应头部信息
# 返回包含正文的可迭代的对象
# 为了更好的理解WSGI框架的工作原理，现在开始着手做这个事情了
# 类Flask框架的实现
# 从现在开始，我们将一步步的实在太忙WSGI的WEB框架的，从面了解WEB框架的内部机制
# WSGI请求environ处理
# WSGI服务器程序会帮我们处理HTTP请求报文
#


from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server,demo_app


def simple_app(environ, start_response):
    setup_testing_defaults(environ)
    status = '200 OK'
    headers = [('Content-Type', 'text/html')]
    start_response(status, headers)
    for k,v in environ.items():
        print(k,v)

    ret = [("%s:%s\n" % (key, value)).encode('utf-8')
           for key, value in environ.items()]
    print(ret )
    return ret


class A:
    def __init__(self,name,age):
        pass
    def __call__(self,environ,start_response):
        pass

class B :

    def __init__(self,environ,start_response):
        setup_testing_defaults(environ)
        status = '200 OK'
        headers = [('Content-Type', 'text/html')]
        start_response(status, headers)
        for k, v in environ.items():
            print(k, v)

        ret = [("%s:%s\n" % (key, value)).encode('utf-8')
               for key, value in environ.items()]
        print(ret)
        self.ret = ret

    def __iter__(self):
        yield from self.ret


# for x in B(environ,start_response):
# for x in simple_app(enumerate,start_response):
# for x in A()(environ,start_response):
#     pass


httpd = make_server('0.0.0.0',8000,simple_app)
httpd = make_server('0.0.0.0',8000,B)

print('SErver on port 8000...')

try:
    httpd.serve_forever()
except:
    httpd.server_close()

