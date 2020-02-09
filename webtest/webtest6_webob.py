from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server, demo_app
from urllib.parse import parse_qs
from webob import Request, Response


def simple_app(environ, start_response):
    request = Request(environ)

    query_string = request.query_string
    method = request.method
    print(query_string,method)
    print(request.GET)
    print(request.POST)
    print(request.path)
    print(5555555,request.params)
    print(6666666,request.headers)

    resp = Response()
    print(resp.status_code)
    print(resp.status)
    print(resp.headers)
    print(resp.headerlist)



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
