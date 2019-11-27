# 随机产生10个数
# 要求
# 每个数值的取值范围 [1,20]
# 统计这20个数中的重复的数字有几个，分别是什么？
# 统计这不重复的数字有几？分别是什么？
# 举例10,7,5,11,6,7,4  ，其中2个数字和7个数和11重复，3 个数字和6个数值重复了


lists = [1, 2, 3, 3, 2, 1, 4, 5, 6, 2, 1, 2, 3, 4, 6, 8, 9, 1, 2, 3, 4, 6, 5, 8, 2, 1, 3, 4, 5, 6, 5, 1, 2, 4, 5, 6, 9]

for i in range(0, len(lists)):
    for j in range(0, len(lists) - 1 - i):
        if lists[j] > lists[j + 1]:
            tmp = lists[j]
            lists[j] = lists[j + 1]
            lists[j + 1] = tmp

for i in lists:
    print(i, end=' ')

print()
print('============================================')
tmp = -1
count = 0
list2 = []
for i in lists:
    if i == tmp:
        count += 1
    if i > tmp:
        if i != 1:
            list3 = [tmp, count]
            list2.append(list3)
        tmp = i
        count = 1
list3 = [tmp, count]
list2.append(list3)

for i in list2:
    print(i)
