# r ： 缺省的，表示只读打开
#  如果存在文件，直接覆盖掉
# open 默认是用一个只读的模式来打开一个已经存在的文件
# w  表示只写方式打开，如果读取则抛出异常
# 如果文件存在，则直接清空文件，如果文件不存在，则创建文件
# x : 文件不存在，就创建，如果文件已经存在，则抛出异常
#

f = open('test3', 'x')


print(f.write('啊'))
#print(f.read())

f.close()
