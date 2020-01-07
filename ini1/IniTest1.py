import configparser
filename = 'test.ini'
# 在内存中创建了一个，返回都全部是空的，如果不提供方法，是如何从外面获取呢？read
# cfg reader ,reader filename ,读取文件，如果不，file
cfg = configparser.ConfigParser()
cfg.read(filename)
sections = cfg.sections()
print(sections)

for sect in sections:
    print(sect,type)
    b = cfg.options(sect)
    for c in b :
        val = cfg.get(sect,c)
        print( sect,' / ',c,'=' ,val)

    print('-----------------------------------------')

#



# 对sample 文件进行不区分大小写的单词统计
# 要求用户可以排除一些

# 实现ls命令功能，实现-l,-a 和--all，-h 选项
# 实现显示路径下的文件列表
# -l 显示详细信息
# -h 和-l配合，人性化的实现
# c 字符 ，d目录，普通文件，l软链接 ，b 块设备，s socket 文件，p pipe 文件，即FIFO
# -rw ,-rw-r-- 1 python python OCt 25000 test
# mode 硬链接 ，属主 属组
# 要求详细列表显示时，时间可以按照 "年-月-日 时:分:秒"
# 排序结果是很少的，如果当前内存中的数据，是如何实现的
#
#