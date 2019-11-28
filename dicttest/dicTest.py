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
print(id(d[0]),id(d[1]))

# 用映射来实现一个值

# 可以 hash 就可以作为 key
# 元组是不一定可以
# 常见的是可以的

# print(id(d[0]),id(d[5])) 只要是 key 那么就必须唯一





