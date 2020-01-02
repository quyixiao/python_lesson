from pathlib import Path

print(Path().joinpath('a', 'b', 'c/d'))

Path() / 'a/b/c/d'.join(['a', 'b', 'c/d'])
#Path 对象/Path 对象
# Path 对象/ 字符串或者字符串/ Path对象
# 分解
# parts 属性，可以返回路径中的第一个部分
# joinpath
# joinpath(*other) 连接多个字符串到Path对象中
# p = Path() # 当前目录
# p = Path('a','b','c/d') 当前目录下的a/b/c/d
# p = Path('/etc')
#路径的拼接和分解
#

