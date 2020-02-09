from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server, demo_app
from urllib.parse import parse_qs
from webob import Request, Response


from webob.multidict import  MultiDict
md = MultiDict()
md.add('a',1)
md.add('b',2)
md.add('b',3)
md.add(1,100)
md.add(1,200)
md.add(2,200)

#print(md)
print(md[1])
print(md.get('b'))
print(md.getall('b'))