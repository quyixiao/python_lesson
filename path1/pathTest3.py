# 这个函数返回的是一个可迭代对象，如果直接调用这个函数返回的是一个
from pathlib import Path

p3 = Path('/Users/quyixiao/python_lesson/path1/a/b/c/d/tomcat.conf')
print(p3.cwd())
print(p3.as_uri())  # 获取这个文件，如果不存在这个文件 ，只要操作完成，目录对象
print(p3.parents[len(p3.parents) - 1])
it = p3.parents[len(p3.parents) - 2].iterdir()  # 迭代当前目录中的所以的文件目录，不进入到子目录中去
for x in it:
    print(x)

p6 = Path('/Users/quyixiao/python_lesson/path1/x/y/z')

print(p6.iterdir())  # <generator object Path.iterdir at 0x112ed18d0>
p6.mkdir(parents=True, exist_ok=True)  # 在有些情况下，目录的长度是有限制的，

for x in p6.iterdir():
    print(x)

p2 = Path()

a = list(p2.glob("_*"))

print(a)
