# 冒泡排序
# 属于交换排序
# 两两比较大小，交换位置，如同水泡上冒
# 结果分为升序和降序排序


# 升序
# 选择排序
lists = [1, 4, 5, 2, 6, 9, 8]
count = len(lists)
for i in range(0, count):
    for j in range(i + 1, count):
        if lists[i] > lists[j]:
            lists[i], lists[j] = lists[j], lists[i]

print(lists)

print('======================================================')

lists = [1, 4, 5, 2, 6, 9, 8]
for i in range(0, count):
    for j in range(count - 1 - i):
        if lists[j] > lists[j + 1]:
            tmp = lists[j]
            lists[j] = lists[j + 1]
            lists[j + 1] = tmp

print(lists)