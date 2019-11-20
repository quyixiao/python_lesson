triangle = [[1], [1, 1]]

n = 6
for i in range(2, n):
    newline = [1]  # 新行及第一个元素
    pre = triangle[i - 1]
    # 1 2 1
    for j in range(0, i - 1):
        val = pre[j] + pre[j + 1]
        newline.append(val)
    newline.append(1)
    triangle.append(newline)

length = len(triangle)
k = 0
for t in triangle:
    print('  ' * ((length - k) // 2), end='')
    print(t)
    k += 1
