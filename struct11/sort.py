s = {1, 2, 3, 1, 2, 3, 4, 5}  # 创建一个一般的集合


print(type(s))
print(s)

li = [1, 2, 3, 1, 2, 3]
li.append(5)
l = list(set(li))
l.sort(key=int,reverse=True)
print(l)

print('##############list0 和list1 是一个引用对象 ############')
list0 = list(range(4))
list2 = list(range(4))

print(list0 == list2)       #list0 和list2 是内容相同
list1 = list0
list1[2] = 10
print(list0)
print(list1)
print(list2)

print('#######################################')




