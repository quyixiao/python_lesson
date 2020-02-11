from wsgiref.simple_server import make_server
from webarch import App
# 拦截器interceptor
# 拦截器，就是要在请求处理环节的某处加入处理，有可能是中断后续处理
# 根据拦截点不同，分为
# 1.请求时拦截
# 2.响应时拦截
#
if __name__ == '__main__':
    httpd = make_server('0.0.0.0', 8000, App())
    print('SErver on port 8000...')
    try:
        httpd.serve_forever()
    except:
        httpd.server_close()
