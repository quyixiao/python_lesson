from .web import Router,App
from webob import Request,Response
from webarch.template import render

# 创建 Router 对象
idx = Router()
py = Router('/python')
# 注册
App.register(idx, py)


@idx.get(r'^/$')
def indexhandler(request: Request):
    print(request.groups)
    print(request.groupdict)
    return 'indexhandler'


@py.get(r'/{id:int}')  # 支持所有的方法访问 ,'/{id:int} #=> '^/(?P<id>\d+)$'
def pythonhandler(request: Request):

    d = {'userlist': [
        (1, 'tom', 20),
        (2, 'jerry', 23),
        (10, 'sam', 30)

    ]}

    res = Response()
    res.json = d
    #return render('index.html', d)
    return res
