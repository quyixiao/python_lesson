# 支持python,Ruby,Java ,C / C ++ 等人多语言，宣称 比 google protocol buffers 还要快4倍
# 兼容 json 和 pickle
# 常用的方法
# MessagePack 简单易用，高效压缩的的协义，
import json

import msgpack

d = """{"a": null, "b": true, "c": false, "d": [1, "abc"], "f": {"a": 1, "b": 2}}"""
j = json.dumps(d)
m = msgpack.dumps(d)
print('json = {},msgpack={}'.format(len(j),len(m)))
print(j.encode(),len(j.encode()))
print(m)


u = msgpack.unpackb(m)
print(type(u),u)


u = msgpack.unpackb(m,encoding='utf-8')
print(type(u),u)


#mesagePack   简单，已经序列化和反序列化的本质是什么，json 这种文本的方式来实现，
# Python 中的序列化，反序列化的方式
#
# RPC 调用，zero RPC 的使用
# 序列化和反序列化
#