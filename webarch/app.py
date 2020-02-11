from wsgiref.simple_server import make_server
from webarch import App

if __name__ == '__main__':
    httpd = make_server('0.0.0.0', 8000, App())
    print('SErver on port 8000...')
    try:
        httpd.serve_forever()
    except:
        httpd.server_close()
