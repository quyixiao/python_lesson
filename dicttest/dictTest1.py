d = {1: 1, 2: 2}
for key in d.keys():
    print(key)

# print values 如何打印数值

for value in d.values():
    print(value)

for item in d.items():
    print(item)

for item in d.items():
    print(item[0], item[1])

for k, v in d.items():
    print(k, v)

for k, _in in d.items():
    print(k)

for _, value in d.items():
    print(value)

# 总结
# python3 中的 keys，value
# 但是这个东西是一个
#
print('=============================================')

# 在迭代的过程中是不允许动的
#for k in d:
# print(k)
# d.pop()
# 表示一个个的移除, 当你在迭代的过程中，如果你在 for 循环之后，如果修改字典的长度，那是不允许的

while(len(d)):
    d.popitem()



for k in d:
    print(k)

print('+++++++++++++++++++++++++++++++++++++++++++++++++++')

d = dict(a = 1 ,b = 2 ,c = 3 ,d = 'str1')
lst = []
for k in d.keys():
    print('=============',k)
    if isinstance(d[k],str):
        lst.append(k)
for k in lst:
    d.pop(k)



# 在迭代的过程中是不能遍历和移除元素
# RuntimeError: dictionary changed size during iteration
#for k in d :
#    d['1000'] = 100


# key 的要求和 set 的元素要求一致
# set 的元素可以就是看做 key ,set 可以看做是 dict 的简化版本
# hashcode 可哈希才可以作为 key,可以使用 hash() 测试
# d = {1:0,2.0:3 ,'abc' : None,('hello','word','python'): 'string',b'abc':135},

