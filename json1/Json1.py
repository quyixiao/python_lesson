import json


d = dict(zip('abcdf',[None,True,False,[1,'abc'],{'a':1,'b':2}]))

s = json.dumps(d)

print(s,type(s))

s1 = """{"a": null, "b": true, "c": false, "d": [1, "abc"], "f": {"a": 1, "b": 2}}"""

print(s1)

d1 = json.loads(s1)

print(d1) # 看着像，但是完全不一样的东西，javaScript 中，非内存的形式来实现
# 我们依然用这种方式来认为是序列化的过程
# 将他转换成内存中的对象
#


