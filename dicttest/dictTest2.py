import random
from collections import defaultdict
from collections import OrderedDict

d = {}
for c in 'abcde':
    for i in range(5):
        if not d.get(c):
            d[c] = []
        d[c].append(str(i))

d = {}
for c in 'abcde':
    for i in range(5):
        if c not in d.keys():
            d[c] = []
        d[c].append(str(i))

for k, v in d.items():
    print(k, v)

print('===============================================')
d = defaultdict(list)
for c in 'abcd':
    for i in range(random.randint(1, 5)):
        d[c].append(i)

for k, v in d.items():
    print(k, v)

# 有序字典
od = OrderedDict(a=1, b=2, c=3, d=4)
for k, v in od.items():
    print(k, v)



#应用场景，我们东西是是这样的，字典是可变的，
# 这种代码我们觉得这是一个东西是
# 字典必须会用，如果 ,这个是不是可以的
# 但是这个是不是一个好的东西的，但是这个东西是好的，



# 用户输入一个数字
# 如果数字存在，则直接输入一个数字
# 真的不能用列表来实现吗？

# 随机产生100个整数
# 数字范围[-1000,10000]
# 升序输出所有的不同的数字及其重复的次数
# 字符统计重复统计
# 字符表'abcdefghijklmnopqrstuvwxyz'
