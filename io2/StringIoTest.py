

from io import StringIO

from io import BytesIO



sio = StringIO() # od
# print(sio.readable(),sio.seekable(),sio.writable())
#
# sio.write("hello word")
# print(1,sio.read())
# io 模块中的类
# from io import StringIO
# with StringIO() as sio:
#     print(sio.write('magedu'))
#     #print(sio.seek(0))
#     #print(sio.read())
#     print(sio.getvalue()) # 这个是在内存中，使用的速度非常的快

# 如果不需要，持久化的东西，内存的使用是非常的快的，带字符的文件，
# 一般来说，减少磁盘的过程，可以大大的提高运行效率
# 是固态的硬盘的话，减少磁盘io的过程，心要的时候，必需要持久化
#

# with BytesIO() as sio:
#     print(sio.write(b'magedu'))
#     print(sio.seek(0))
#     print(sio.read())
#     print(sio.getvalue()) # 这个是在内存中，使用的速度非常的快


from sys import stdout
f = stdout #
print(f.readable(),f.seekable(),f.writable()) # 都是类文件对象，网络设备也是文件，linux 中 ，一切皆文件，在linux 中，一切都是类文件对象

f.write('abc')

print(type(f)) # 这个是一个文本包装的对象




