# 自己实现一个函数，实现base64
# 索引，对应的字符，索引 ，对应的字符 ，索引 ，对应的字符
# 输入每三个字节断开，拿出一个3个字节，每6个 bit 断开成4段
# 2 ** 6 = 64 ，因此有了 base64的编码表
# 每一段当做一个8bit 看它的值，这个值就是 Base64 编码表的索引值，找到对应的字符 ，再取3个字节，同样的处理，直到最后
# 举例
# abc 对应的 ASCII 为0x610x620x63
# 末尾处理，
# 1 正好3个字节，处理方式同上
# 2 剩1个字节或者2个字节，用0补满3个字节
# 3 补0的字节用=表示
# 在 python 的运行环境下进行的，优化完成了以后，就差不多的，
# 如果说 java 语言，如果你写的是 c 和c ++ 是不做这些优化的
# 看谁的执行时间是好的
# 上面和下面的东西
#  位操作还是有用的，什么是 byte

import base64

alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz+/";

teststr = "abcd";

# testStr = "Manma"


print(0x3F)
print(0x3D)


def my_base64(src):
    ret = bytearray()
    length = len(src)
    r = 0
    for offset in range(0, length, 3):
        if offset + 3 <= length:
            triple = src[offset: offset + 3]
        else:
            triple = src[offset:]
            r = 3 - len(triple)
            triple = triple + '\x00' * r  # 补几个0
        # print(triple,r)
        # 将3个字节看成一个整体转成字节 bytes ,大端模式
        # abc => 0x616263

        b = int.from_bytes(triple.encode(), 'big')  # 小端模式为'little'
        print('-------------',hex(b))
        print('=================' ,b )
        # 01100001 01100010 01100011 # abc
        # 011000 010110 001001 100011 第6位断开
        #
        #
        for i in range(18, -1, -6):
            if i == 18:
                index = b >> i
            else:
                index = b >> i & 0x3F  # 0b0011 1111  0x3F  = ?
            ret.append(alphabet[index])  # 得到 base64 编码列表
        # 策略是不管是不是堆零，都填满，只有最后一次可能出现补零的，
        # 在最后替换掉的就是了，代码清晰，而且替换至多2次
        # 在上一个循环中判断 r != 0 效率可能会高一些

        for i in range(1, r + 1):  # 1 到 r ，补几个0替换第几个 =
            ret[-i] = 0x3D  # 3D = = 号

    return ret


print(my_base64(teststr))

print(base64.b64encode(teststr.encode()))
