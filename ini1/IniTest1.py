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

