

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
# 文本模式支持从开头偏移
# whence 为1 表示从当前位置开始偏移，但是只支持偏移0，相当于原始于
# 文件指针，指向当前字节的位置
# mode = r, 指针起始于0
# mode = a ,指针起始于EOF
# tell() ,显示指针当前位置
# seek()(offset[,whence])
# 移动文件指针的位置，offeset偏移多少字节，whence 从哪里开始
# 文本模式位置
# whence 0 缺省值，表示从开始，offeset只能从正数
# whence 1 表示从位置，offeset只接受0
# whence 2 表示从EOF开始，offset 只接受 0
#


f = open('test3','r+')

print(f.read())
print(f.tell())
print(f.write('983288932'))
f.seek(0)
print(f.read())
f.close()








