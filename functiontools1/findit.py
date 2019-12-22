s1 = 'abcdefg'
s2 = 'defabcdoabcdeftw'
s3 = '1234a'
s4 = "567812"
s5 = 'abcdd'


def findit(str1, str2):
    matrix = []
    # 从x 轴或者 y 轴取都可以的，选择 x 四 ，xmax 和 xindex
    xmax = 0
    xindex = 0
    for i, x in enumerate(str2):
        # 我觉得还是这个好的，因为他们不确定这个东西是什么的
        matrix.append([])
        for j, y in enumerate(str1):
            if x != y:  # 若两个字符不相等
                matrix[i].append(0)
            else:
                if i == 0 or j == 0:  # 两个字符不相等，有字符在边上
                    matrix[i].append(1)
                else:  # 不在边上
                    matrix[i].append(matrix[i - 1][j - 1] + 1)
                if matrix[i][j] > xmax:  # 判断当前加入的值和记录的最大值是否相等
                    xmax = matrix[i][j]  # 记录最大的值，用于下次比较
                    xindex = j  # 记录当前值的 x 轴偏移量
                    xindex += 1  # 只为计算的需要才加1 和 str1[xindex - xmax : xindex] 匹配

    #  return str1[xindex+1 -xmax :xindex + 1 ]
    return str1[xindex - xmax: xindex]


print(findit(s1, s2))
print(findit(s1, s3))
print(findit(s3, s4))
print(findit(s3, s4))
print(findit(s1, s5))
# 如何取子串，只要找到一个就可以了，不是负一就找到了，像这种东西，
#

