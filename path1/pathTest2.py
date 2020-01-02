from os import  path
# p = path.join('/etc','/sysconfig','/network','/Users/quyixiao/sl')
# print(type(p),p)
# print(path.exists(p))
# print(path.split(p))
# print(path.abspath('.'))
#
# print(path.dirname(p))
# print(path.basename(p))
# print(path.splitdrive(p))
#
#
#
# p1 = path.abspath(__file__)
# print(p1,path.basename(p1))
# while p1 != path.dirname(p1):
#     p1 = path.dirname(p1)
#
#
from pathlib import Path

p = Path()
print(p.absolute())
print(type(p))
print(str(p))

print(p)
p1 = p / 'a'/ 'b' / 'cd';
print(p1)


p = Path() # 当前目录，
p = Path('a','b','c','d/e')
p = Path('/etc')
print(p)
