import re

pattern = r'{{([^{}]+)}}'
regex = re.compile(pattern)

def repl(matcher):
    return str(d.get(matcher.group(1),''))
d = {
    'id': 50,
    'name': 'tom',
    'age': 20
}

with open('index.html', encoding='utf-8') as f:
    for line in f:
        ret = regex.sub(repl, line)
        print(ret)
