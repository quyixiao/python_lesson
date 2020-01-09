import re

# match ,search函数可以返回 match对象， findall 返回字符串列表，finditer 返回一个个 match对象，
#  如果 pattern 中使用了分组，如果有匹配的结果，会在 match 对象中
# 1.使用了 group(N) 方式返回对应的分组，1-N是对应的分组，0返回整个匹配的字符串
# 2.使用命名分组，可以使用 group('name')的方式取分组
# 3.也可以使用 groups()返回所有组
# 4.使用 groupdict() 返回所有命名的分组
#
s = '''bottle\nbag\nbig\napple\nboss'''
for i, c in enumerate(s, 1):
    print((i - 1, c), end='\n' if i % 8 == 0 else ' ')

print()
print('----------------------------------------')

#matcher = re.match('(b)(\w+)\n(b\w+)', s)
matcher = re.match('b\w+\n(?P<g2>b\w+)', s)

print(matcher)

print(matcher.groups())
print(matcher.group(0))
# print(matcher.group(1))
# print(matcher.group(2))
# print(matcher.group(3))
print(matcher.groupdict())
