# os.name windows是nt,linux 是posix
# os.uname linux 支持
# sys.platform window显示window3
#
import os
import shutil
import sys
from pathlib import Path

print(sys.platform)
print(os.uname())
print(os.name)


# os.chmod('test',0o777)
# os.chown(path,uid,gid)
#

#  """copy data from file-like object fsrc to file-like object fdst""" 表示复制一个文件对象，加一个w就可以了
with open('test','r') as src :
    with open('test1','w+') as dest :
        shutil.copyfileobj(src,dest)


#shutil模块
# 到目前为止
# 文件拷贝，使用打开2个文件对象，源文件读取的内容，写入目标文件中来完成拷贝过程，
# 如果路径是一样的，那就没有太大的区别的，相同的，相同的文件，绝对路径是不是同一个，如果不是相同的文件就可以向下走
#

st = Path().stat()
print(type(st))


