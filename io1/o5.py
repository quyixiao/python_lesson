

# 以mode and at most one plus
f = open('test','wb')
#print(f.write('啊'.encode())) # 将一个中文转换成字节


print(f.write('啊'.encode(encoding='utf-8')))

f.close()



