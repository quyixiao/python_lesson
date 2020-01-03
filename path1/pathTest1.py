from pathlib import Path

print(Path().joinpath('a', 'b', 'c/d'))

p2 = Path() / 'a/b/c/d'.join(['a', 'b', 'c/d'])
# Path 对象/Path 对象
# Path 对象/ 字符串或者字符串/ Path对象
# 分解
# parts 属性，可以返回路径中的第一个部分
# joinpath
# joinpath(*other) 连接多个字符串到Path对象中
# p = Path() # 当前目录
# p = Path('a','b','c/d') 当前目录下的a/b/c/d
# p = Path('/etc')
# 路径的拼接和分解
#


# for t in p2.parents:
#     print(t)


print(p2.parents[len(p2.parents) - 1])

p3 = Path('a/b/c/d/tomcat.conf')
print(p3.name)
print(p2.name)

print(p3.home())
print(p3.stem)
print(p3.suffix)
print(p3.with_name('nginx.conf')) # 替换名字
print(p3.with_suffix('.xml')) # 替换后缀
print(p3.suffixes) # 所有的后缀
p4 = Path(str(p3) + '.xml') # 多个后缀
print(p4)# a/b/c/d/tomcat.conf.xml 将原来的东西，变成自己的东西
print(p4.suffixes)

print(p4.cwd())# 返回当前工作目录
print(p4.home())# 返回当前的家目录
print(p4.is_dir()) # 是否是目录，文件
print(p4.is_file()) # 是否是一个文件
print(p4.is_symlink()) # 是不是一个软链接
print(p4.is_socket()) # 是不是一个socket 文件
print(p4.is_block_device()) # 是不是一个块设备
print(p4.is_char_device()) # 是不是一个字符设备
print(p4.is_absolute()) # 是不是一个抽象路径 是一个绝对的路径，还是一个抽象的路径，管道文件，如果不是继承的方式是不一样的，还有一个方法
print(p4.resolve()) #  这个找的是软链接的真正的东西，
print(p4.absolute())
print(p4.exists()) # 存在不？
print(


)
#















