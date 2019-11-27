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
