# 简单的排序
# 属于选择排序
#
lst = [1, 9, 8, 5, 6, 7, 4, 3, 1, 2,3,4,5,2]
length = len(lst)
for i in range(length):
    maxindex = i
    for j in range(i + 1, length):
        if lst[j] > lst[maxindex]:
            maxindex = j
    lst[i], lst[maxindex] = lst[maxindex], lst[i]

for i in lst:
    print(i, end=' ')




#{[x] for x in range(5)}
