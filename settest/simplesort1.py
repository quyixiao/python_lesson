# 简单的排序
# 属于选择排序
# 简单的选择排序需要数据一轮轮比较，并在每一轮中发现极值
# 没有办法知道当前轮是否已经达到排序要求，但是可以知道极值
lst = [1, 9, 8, 3, 2, 5, 4, 5, 2, 3, 1, 3, 4, 5, 6, 5, 2, 1]
length = len(lst)

for i in range(0, length // 2):
    maxindex = i
    minindex = -i - 1
    minorigin = minindex
    for j in range(i + 1, length - i):
        if lst[maxindex] < lst[j]:
            maxindex = j
        if lst[minindex] > lst[-j - 1]:
            minindex = - j - 1
    if i != maxindex:
        lst[i], lst[maxindex] = lst[maxindex], lst[i]
        if i == minindex or i == length + minindex:
            minindex = maxindex

    if minorigin != minindex:
        tmp = lst[minorigin]
        lst[minorigin] = lst[minindex]
        lst[minindex] = tmp

for i in lst:
    print(i, end=' ')
