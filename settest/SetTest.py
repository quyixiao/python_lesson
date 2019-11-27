# 约定
# set翻译为集合
# collection 翻译为集合类型，是一个大概念
# set 是一个可变的，无序的，不重复的，元素的集合

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
# 元素不可以索引
# set可以迭代
# s7 = {[1],(1,),1} # ?
