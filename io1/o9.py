


f = open('test','r+')
print(f.read().encode())
f.seek(0)
print(f.readlines())
f.seek(0)

for line in f.readlines():
    print(line.strip())

f.seek(0)
print(f.readlines(1))
print(f.readlines(1))
print(f.readlines(1))
f.close()




#对于类似文件对象的IO对象，一般来说，都需要不使用的时候关闭，注销，以释放资源，IO被打开时候，会获得一个文件对象，





with open('test5') as f : #如果出现异常的话，保证文件对象被释放掉。对操作系统而言，资源会还回来
    f.read()
    f.write()


#


print('1111111111111')


# 指定一个文件，实现copy 到目标文件


#文件自己写字符串的时候，我们自己控制，我们应该在做的时候
#

# 请大家帮我统计一多少个单词

# public void main(){
# 
#}
