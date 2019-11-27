# 求杨辉三角的第m行的k个元素


lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# print(len(lists))
# 根据对角线来

for i in range(0, len(lists)):
    for j in range(0, len(lists[i])):
        print(lists[j][i], end=' ')
    print('')

print('===================================================')
matrix = [[1, 2, 3, 10], [4, 5, 6, 11], [7, 8, 9, 12], [1, 2, 3, 4]]
length = len(matrix)
count = 0
for i in range(length):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        count += 1

print(matrix)
print(count)
