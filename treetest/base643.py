# 自己实现 base64 解码函数
# 完美命令分发器
# 要求函数可以带参数（不考虑可变参数，keyword-only参数）
# 用户输入命令，执行相应的函数
#
# www.magedu.com
# base64 解码实现
import base64

from collections import OrderedDict

base_tbl = b"ABCDEFGHIJKLMNOPQRSTUVwXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
alphabet = OrderedDict(zip(base_tbl, range(64)))


def base64decode(src: bytes):
    ret = bytearray()
    length = len(src)
    step = 4
    for offset in range(0, length, step):
        tmp = 0x00
        block = src[offset:offset + step]
        # 开始计算
        for i in range(4):
            # 替换字符为序号
            index = alphabet.get(block[-i - 1])
            if index is not None:
                tmp += index << i * 6

        ret.extend(tmp.to_bytes(3, 'big'))
    return bytes(ret.rstrip(b'\x00'))  # 把最右边的0x00 去掉，不加变


txt = "TWFU"
# txt = "TWE="
txt = txt.encode()
print(txt)

print(base64decode(txt).decode())
print(base64.b64decode(txt).decode())








