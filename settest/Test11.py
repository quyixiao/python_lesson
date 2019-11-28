a = [1, 9, 7, 5, 6, 7, 8, 8, 2, 6]
b = [1, 9, 0, 5, 6, 4, 8, 3, 2, 3]

#
s1 = set(a)
s2 = set(b)
print(s1)
print(s2)
print(s1.union(s2))  # 联合问题 ，两个联合问题
print(s1.symmetric_difference(s2))  # 没有的  ，不重复的数值
print(s1.intersection(s2))  # 公共的 重复的数值是
