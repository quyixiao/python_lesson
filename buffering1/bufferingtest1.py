# -1 表示使用缺省的大小的buffer ，如果是二进制模式，使用io.DEFAULT_BUFFER_SIZE 的值，默认是4096值
# 或者是8192，如果是文本械，如果是终端设备，是行缓存方式，如果不是，则使用二进制模式的策略
# 0 只在二进制模式的使用，表示关buffer
# 1 只在文本的模式中使用，表示使用缓冲，意思就是见到换行符就是flsh
# 大于1 用于指定buffer 的大小
# buffer 缓冲区
# 缓冲区 一个内存空间，一般来说是一个FIFO队列，到缓冲区满了或者达到阈值，数据才会flush到磁盘
# flush() 将缓冲区数据写入到磁盘
# close() 关闭前会调用flush()
#
import io

print(io.DEFAULT_BUFFER_SIZE)
f = open('test','w+')
f.write('!'*1024)
f.seek(0)
print(f.tell())
#print(f.read())
f.close()

