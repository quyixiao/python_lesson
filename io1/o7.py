#newline
# 什么样的编码错误将被捕获
# None 和strict表示有编码错误，将抛出ValueError,ignore表示忽略
#
# f = open('test','w')
# f.write('abc\n9832983298\roiew9iew98\r\n')
# f.close()

newlines = [None,'','\r','\n','\r\n']
for n1 in newlines:
    f = open("test",newline = n1)
    print('-------------------' ,f.read().encode())
    print(f.fileno()) # 文件描述符，文件，操作文件，文件，
    f.close()

