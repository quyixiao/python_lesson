from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server, demo_app
from urllib.parse import parse_qs
from webob import Request,Response





def simple_app(environ, start_response):
    setup_testing_defaults(environ)
    query_string = environ.get('QUERY_STRING')
    d = {}
    for item in query_string.split('&'):
        k, _, v = item.partition('=')
        print(k, v)
        d[k] = v

    d = {k: v for k, _, v in map(lambda x: x.partition('='), query_string.split('&'))}
    print(d)

    qs = parse_qs(query_string)
    print(1111111,qs)

    method = environ.get('REQUEST_METHOD')
    print(method) # 获得get方法
    #



    status = '200 OK'
    headers = [('Content-Type', 'text/html')]
    start_response(status, headers)
    return [query_string.encode()]


httpd = make_server('0.0.0.0', 8000, simple_app)

print('SErver on port 8000...')
try:
    httpd.serve_forever()
except:
    httpd.server_close()
