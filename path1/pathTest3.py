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
# 通配符
# glob(pattern) 通配给定的模式
# rglob(pattern) 通配给的模式，递归目录
# 返回一个生成器
# list(p.glob('test.*')) # 返回当前目录的对象下的test开头的文件
# list(p.glob('**/*.py')) # 递归所有的目录，等同于rglob()
# g = p.rglob('*.py') # 生成器
# next(g)
# 匹配 ，成功返回True
#
print(Path('a/b.py').match("*.py"))
print(Path('a/b/c.py').match("b/*.py"))
print(Path('a/b/c.py').match("a/*.py"))
# stat() 相当于stat命令
# lstat() 这个是看软链接的信息， 同 stat() ，但是如果符号相同 ，则这个东西转化成十进制
# 这个拿过来之后，能不能用呢？如果想看软链接本身的话，则提供了文件的操作
# p2.open() 使用方法类似内建函数open,返回一个文件的对象
# 增加新的函数
#
# Path.read_text() # 这个表示以文本的模式打开，返回所有内容
# Path.read_bytes() #  这个表示以字节的形式打开 ，这个表示 这个表示以字节的形式读取内容
#
# Path.write_bytes() 表示以写的形式来写数据，
# 把你的数据给我，我直接写出去就可以了
#

p = Path('my_file')
p.write_bytes(b'893298899832')
print(p.read_bytes())
p = Path('my_text_file')
p.write_text('工9832983982893')
p.read_text()












