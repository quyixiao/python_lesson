

# a  表示 append ，a  表示,如果没有一个文件，则直接追加，如果文件存在，则从尾部追加
# w # 表示文件存在不存在， 如果 x 表示，如果文件存在，则直接抛出异常
# w x a , a w 直接清除，a 表示追加
# 文本模式， 操作方式是
# t 表示是默认的模式，t 默认的都是，
# b 表示进制模式，
# 文件就是按照字节来理解，与字符编码没有关系，二进制模式操作时，字节操作
#


f = open('test4','a')


#print(f.read())
f.write("xxx")


f.close()



