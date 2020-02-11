import re
from io import StringIO

pattern = r'{{([^{}]+)}}'
regex = re.compile(pattern)

d = {
    'id': 50,
    'name': 'tom',
    'age': 20
}


def repl(matcher):
    return str(d.get(matcher.group(1), ''))


# <p>{{id}} {{name}} {{age}}</p>
def parse(line: str, data: dict):
    start = 0
    res = ''
    for matcher in regex.finditer(line):
        print(matcher)
        res += line[start:matcher.start()]
        res += str(data.get(matcher.group(1), ''))
        start = matcher.end()
    else:
        res += line[start:]
    return res


out = StringIO()

with open('../webarch/templates/index.html', encoding='utf-8') as f:
    for line in f:
        # ret = regex.sub(repl, line)
        ret = parse(line, d)
        out.write(ret)

print('------------------------------')
print(out.getvalue())
