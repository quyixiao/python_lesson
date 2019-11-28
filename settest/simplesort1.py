# 简单的排序
# 属于选择排序
#
lst = [1, 9, 8, 5, 6, 7, 4, 3, 1, 2, 3, 4, 5, 2]
length = len(lst)
for i in range(length // 2):
    maxindex = i
    minindex = i
    for j in range(i + 1, length):
        if lst[j] > lst[maxindex]:
            maxindex = j
        if lst[j] < lst[minindex]:
            minindex[j]
    lst[i], lst[maxindex] = lst[maxindex], lst[i]
    lst[2*i] ,lst[minindex] = lst[minindex] ,lst[2 * i ]
for i in lst:
    print(i, end=' ')
