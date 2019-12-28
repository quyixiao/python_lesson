

# 以mode and at most one plus
# f = open('test','rw')
# #print(f.write('啊'.encode())) # 将一个中文转换成字节
# #ValueError: must have exactly one of create/read/write/append mode
# f.close()

# 为r,w ,a  x提供了缺失的读写功能，但是，获取文件的对象依旧按照 r,w,a x 自己的
#
# open 打开一个文件，这个参数
#

# 文件指针 ，上面的例子中，已经说明了一个指针
# 文件指针，指向当前字节位置
# tell() 显示文件指针当前的位置
# seek(offset)
# end of file
#

f = open('test3','r+')

print(f.read())
print(f.tell())
print(f.write('983288932'))
f.seek(0)
print(f.read())
f.close()








