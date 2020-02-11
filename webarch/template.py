# 模板加载
#

from jinja2 import Environment, PackageLoader, select_autoescape,FileSystemLoader


env = Environment(
    loader=PackageLoader('webarch', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)
#
# env = Environment(
#     loader=FileSystemLoader('templates'),
# )



def render(name,data:dict):
    template = env.get_template(name)
    html = template.render(**data)
    print(html)
    return html
