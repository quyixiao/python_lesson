# key-value 键值对的数据的集合
# 可变的，无序的，key 不重复
# 是不可重复的元素，key 在整个元素中
# dict()

d = {}
d = {'a': 10, 'b': 20, 'c': [1, 2, 3, 4]}
lst = [1, 3, 3]
print(d)
d = dict(a=1, b=2)
print(d)
e = {'234': '123'}
print(e)
print(d)
print('-----------------------------------------')
d = dict(([1, 'a'], [2, 'b']))
print(d)
d = dict.fromkeys(range(5))

print(d)
# 表示是一个引用类型
d = dict.fromkeys(range(5), [1000])

print(d)
#
print(id(d[0]), id(d[1]))

# 用映射来实现一个值

# 可以 hash 就可以作为 key
# 元组是不一定可以
# 常见的是可以的

# print(id(d[0]),id(d[5])) 只要是 key 那么就必须唯一

e = d.get(33)  # 没有返回值,函数是返回的值是，容易出现 key 不存在的情况

print(e)

f = d.setdefault(100, 2)  # 如果不存在的话，则返回默认值，如果存在，则返回之前的默认值
print(f)
f = d.setdefault(100, 3)
print(f)
# d[key] = value
# 将 key 不存在的话，则直接创建一个值
d[38928] = 2002  # 如果 key 存在，就创建，如果 key 不存在，则
print(d)
# 字典是无序的
d.update(red=1)
print(d)
d.update((('red', 2),))
print(d)
d.update({'red': 3})
print(d)
# dict 中 key 一定是唯一的，key 的顺序是无序的
# 字典删除
d.pop(38928)
print(d) #
#  如果什么都没有写的话，随机是可以
key,value =d.popitem()
print(key,value)


d.pop(3289328932,3) # 如果这个值没有的话，就会返回错误
# clear
# 清空字典

a = True
b = [6]
d = {'a':1 ,'b':b }
print(a )
# del a   如果 a 被删除，那么a 删除的是引用
print(a )

