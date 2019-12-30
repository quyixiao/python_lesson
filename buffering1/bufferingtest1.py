# -1 表示使用缺省的大小的buffer ，如果是二进制模式，使用io.DEFAULT_BUFFER_SIZE 的值，默认是4096值
# 或者是8192，如果是文本械，如果是终端设备，是行缓存方式，如果不是，则使用二进制模式的策略
# 0 只在二进制模式的使用，表示关buffer
# 1 只在文本的模式中使用，表示使用缓冲，意思就是见到换行符就是flsh
# 大于1 用于指定buffer 的大小
# buffer 缓冲区
# 缓冲区 一个内存空间，一般来说是一个FIFO队列，到缓冲区满了或者达到阈值，数据才会flush到磁盘
# flush() 将缓冲区数据写入到磁盘
# close() 关闭前会调用flush()
# buffering = -1 t 和 b 都是io.DEFAULT_BUFFER_SIZE
# buffering = 0 b 关闭缓冲区 , t 不支持
# buffering = 1 b 就是一个字节,t行缓冲，遇到换行符才flush
# buffering > 1 b 模式表示行缓冲大小，缓冲区的值可以超过io.DEFAULT_BUFFER_SIZE,直接设定的值超出后才把缓冲区flush ,
#               t 模式，是io.DEFAULT_BUFFER_SIZE ，flush完后把当前的字符串也写入到磁盘中
# 似乎看起来很麻烦，一般来说，只需要记得
# 1.文本模式，一般都是用默认的缓冲大小
# 2.二进制模式，是一个个字节的操作，可以指定buffer的大小
# 3.一般来说，默认的缓冲区的大小是比较好的选择，除非明确知道，否则不调整它
# 4.一般来说，明确的知道需要写磁盘了，都会手动调用一次flush,而不是等到自动的flush,或者close 以后
#

#
import io

print(io.DEFAULT_BUFFER_SIZE)
f = open('test','w+')
f.write('!'*1024)
f.seek(0)
print(f.tell())
#print(f.read())
f.close()

