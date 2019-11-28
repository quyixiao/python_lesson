matrix = [[1, 2, 3], [4, 5, 6]]
# 一次性开辟内存空间比两种内存同时开辟要快得多
# 在原来的矩阵中,将原来的元素使用在这里，所在，列表解析式如何实现
tm = [[0 for col in range(len(matrix))] for row in range(len(matrix[0]))]  # [[0, 0], [0, 0], [0, 0]] 开辟内存空间


#
count = 0

for i, row in enumerate(tm):
    for j, col in enumerate(row):
        tm[i][j] = matrix[j][i]  # 将 matrix 的所有元素搬到 tm中
        count += 1


for i in matrix:
    print(i)

print('========================================')

for i in tm:
    print(i)
print(count)
