# 单向链表，实现，append,itenodes  方法
# 双向链表实现append,pop,insert,remove,iternodes 方法
# 向后追加
# 有一个有序的[37,99,73,48,47,40,40,25,99,51] 请先排序并打印输出
# 分别尝试插入20，40，41 到这个序列中合适的位置，保证其有序
# 思路
# 排序后十分查找到合适的位置插入数值
#  如果存在的话，
origin = [37, 99, 73, 48, 47, 39, 41, 25, 99, 51]
sorted_list = sorted(origin)
nums = [20, 40, 42,100,210,5]
for x in nums:
    for i, v in enumerate(sorted_list):
        if v > x:
            break
    sorted_list.insert(i, x)

print(sorted_list)
