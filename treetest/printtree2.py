# 其他的性质
# 高度为 k 的二叉树，至少有 k 个结点
# 含有 n (n>=1 ) 的结点 的二叉树的高度至多为 n ,最少为 math.ceil(log2(n + 1 )) 不小到数值的最小整数的
# 向上取整
# 二叉树的遍历
# 层序遍历，
# 深度优先遍历
# 前序遍历
# 中序遍历
# 后序遍历
# 每个子树的内部依然是先根结点，再左子树后右子树，递归遍历
# 遍历序列
# A BDGH CEIF

import math


# 投影栅格实现 def print tree (array)

# 前空格元素间

def print_tree(array):
    index = 1

    depth = math.ceil(math.log2(len(array)))  # 因为使用时前面 9 了，不然应该是 math. C eil (math. Log2 (len (array) +1)

    sep = '  '
    for i in range(depth):
        offset = 2 ** i
        print(sep * (2 ** (depth - i - 1) - 1), end='')
        line = array[index: index + offset]
        for j, x in enumerate(line):
            print("{:>{}}".format(x, len(sep)), end='')
            interval = 0 if i == 0 else 2 ** (depth - i) - 1
            if j < len(line) - 1:
                print(sep * interval, end='')
        index += offset
        print()


# Heap Sort

# 为了和编码对应，增加一个无用的在首位

# origin= [0,59,19,90,30,70,40,80,60,20]
origin = [0, 30, 20, 80, 49, 59, 19, 60, 70, 90]

total = len(origin) - 1  # 初始待排序元素个数，即 n

print(origin)
print_tree(origin)

print('-----------------------------------------------')


def heap_adjust(n, i, array: list):
    # 调整当前结点（核心算法)
    # 调整的结点的起点在n/2,保证所有调整的结点都有孩子结点 param n：待比较数个数 param 1: 当前结点的下标
    # Param
    # array：待排序数据

    # return。None

    while 2 * i <= n:

        # 孩子结点判断 2i 为左孩子，2i + 1为右孩子
        lchile_index = 2 * i

        # 先假定左孩子大，如果存在右孩子且大则最大孩子索引就是右孩子
        max_child_index = lchile_index  # n=2i
        if n > lchile_index and array[lchile_index + 1] > array[lchile_index]:  # n > 2i说明还有右孩子
            max_child_index = lchile_index + 1  # n=2 i+1
            # 和子树的根结点比较
        if array[max_child_index] > array[i]:
            array[i], array[max_child_index] = array[max_child_index], array[i]
            i = max_child_index  # 被交换后，需要判断是否还需要调整
        else:
            break


# heap_adjust(total, total // 2, origin)


def max_heap(total, array: list):
    for i in range(total // 2, 0, -1):
        heap_adjust(total, i, array)
    return array


print_tree(max_heap(total, origin))

print(origin)
print_tree(origin)
# 每次都要对大顶堆，只要你向他指向谁，谁在堆顶，90 在堆顶，1 在最后的一个那里交换，
# 在排序之前 ,排序是最后的一个和第一个，有序，一定在堆
# 总结，
# 是利用堆的性质的一种排序，在堆顶选出最大值或者最小值
# 时间时间复杂度
# 堆排序的时间复杂度为 O（nlogn）
# 由于堆排序的原始记录的排序状态并不敏感，因此它无论是最好，还是最坏的情况的复杂度均为 O(nlogn)
# 只是使用了一交换空间的，空间复杂度就是 O(1)
# 稳定性，
#   是不稳定排序算法
#   如果堆排序，堆排序算法，如果对自己有更加高的要求的话，则直接使用，自己实现 base64 的解码
#   解码比编码简单
#


print('=' * 50)


def sort(total, array: list):
    while total > 1:
        array[1], array[total] = array[total], array[1]  # 堆顶和最后一个结点交换
        total -= 1
        if total == 2 and array[total] >= array[total - 1]:
            break
        heap_adjust(total, 1, array)
    return array


print_tree(sort(total, origin))
