# 模板加载
#

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('webarch', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

d = {'userlist': [
    (1, 'tom', 20),
    (2, 'jerry', 23),
    (10, 'sam', 30)

]}

template = env.get_template('index.html')
html = template.render(**d)
print(html)
