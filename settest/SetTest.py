# 约定
# set翻译为集合
# collection 翻译为集合类型，是一个大概念
# set 是一个可变的，无序的，不重复的，元素的集合
# clear() 不理所有的元素
# 修改 ，要么删除，要么加入新的元素
# 为什么要修改呢？
# 查询 非线性结构，无法索引
# 遍历
# 可以迭代所有元素
# 成员运算符
# in 和 not in 判断元素是否在set中
# 效率呢？
# 线性结构的查询时间复杂度是O(n)，即随机数据规模的增大而增加耗时
# set ，dict 等结构，内部使用的是hash 值作为key ,时间复杂度可以做到 O(1) ,查询时间和数据规模无关
# print(hash(1,'abc',[1])) list 不能作为,list 的值是可变的，如果这个值是可变的，那么用这个值作为hash值，没有什么意义
# 可hash
# 数值型int,float,complex
# 布尔型 True,False
# 字符串strings,bytes
# tuple
# None
# 以上都是不可变类型，成为可哈希类型，hashtable
# 差集，集合中除去和其他集合的公共部分
#
# 基本概念
# 全集
# 所有元素集合，例如实数集，所有的实数组成的集合就是全集
# 子集，subset和超集superset
# 一个集合A所有的元素都是在另一个集合B内，A是B集合的子集
# union(*others)
# update(*others)
# 等同于 udpate
# set 是一个可变的，无序的，不重复的，元素集合
# 约定，set翻译为集合。
# collection 翻译为集合类型，是一个大家的概念
# 如果找不到元素，则会抛出异常，随机的从元素中弹出一个元素
# in 和 not in 遍历是无序的，是按照索引来实现的，set  内部使用的是hash 值，时间复杂度可以做到O(1) ,查询时间和数据规模无关

import datetime
import timeit

s = set()
print(type(s))
s = set(range(10))
print(s)
s = {1, 2, 3}
print(s)

s = {}
print(s)
print(type(s))

s = set(list(tuple(map(str, range(5)))))

print(s)

s1 = set()
s2 = set(range(5))
s3 = set(list(range(5)))
print(s3)

print(hash(1))

print(hash((2, 3, 'aaaa')))  # 可以说是一个线性结构

print(hash((2, 3, b'aaaa')))  # 可以说是一个线性结构

# print(hash({(1,2),3,'a'}))
# set 的元素
# set 的元素要求必须是可以hash 的
# 目前学过的不可hash 的类型有list,set
# 元素不可以索引 ,是乱序的，内存中是乱的
# set可以迭代
# s7 = {[1],(1,),1} # ?


# set增加
# add(element)
#   增加一个元素到set中
#   如果元素存在，什么都不做
# update(other)
#
s.add('abc')
print(s)
s.add(0)

s.update(range(5), range(3, 7))
print(s)
s.add('bcd')
print(s)
s.update('bcd', '123')
print(s)
s.add(-1)
print(s)

s.remove('bcd')

print(s)

print(s.discard('bcd'))  # discard(element) 从set移除一个元素，元素不存在，将什么都不做

print(s.discard(0))

print(s)
s.pop()  # 弹出一个元素，随机弹出一个元素
print(s)

s.clear()

print(s)

if 5 in [4, 5, 6]:
    pass

if 5 in (5, 6):
    pass

lst1 = list(range(100))
lst2 = list(range(1000000))

# timeit (-1 in lst2)  set的速度比list 的时间快得多

print(hash(1))
print(hash('1'))
print(hash(0b1111))
print(hash('abcdefgh'))

start = datetime.datetime.now()

print(-1 in set(range(10000009)))

end = datetime.datetime.now()
print(end - start)

print(hash(tuple([1, 2])))

# 交集
# intersection(* others )
# 返回和多个集合的交集
# & 等同于 intersection
# intersection _update(* others)
#   获取多个集合交集并修改
#   等同于difference _update
#   交集用于and
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 > s2)
print(s1 < s2)

print(s1 == s2)

s1.add(4)
s2.add(2)

print(s1)

# isdisjoint 是不是有交集

print(s1.isdisjoint(s2))
print(s1 & s2 == set())
s1.clear()

print(s1 & s2 == set())


# 集合应用
# 共同好友，求共同好友
# 有一个api,要求权限具备
# hash(tuple(1,'abc',[1]))
set1 = {'A', 'B', 'C'}
set2 = {'e', 'f', 'D', 'C'}
set3 = set1 & set2
if set3 == set():
    print('xxx 与群里的其他人没有微信朋友关系')
else:
    print('xxx 与群里的其他的人有朋友关系')
