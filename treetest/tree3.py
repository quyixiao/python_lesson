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


# 居中对齐方案

def print_tree(array, unit_with=2):
    length = len(array)  # 9
    depth = math.ceil(math.log2(length + 1))
    index = 0
    width = 2 ** depth - 1  #
    for i in range(depth):
        for j in range(2 ** i):
            # 居中打印，后面加一个空格
            print('{:^{}}'.format(array[index], width * unit_with), end=' ' * unit_with)
            index += 1
            if index >= length:
                break
        width = width // 2  # 居中打印宽度减半
        print()  # 控制换行




origin = [0,30,20,80,40,50,10,60,70,90]
total = len(origin) -1 #初始排序的元素的个数，即 n
print(origin)
print_tree(origin)


def heap_adjust(n,i,array:list):
    """
    调整当前结点（可以算法）

    :param n:
    :param i:
    :param array:
    :return:
    """





