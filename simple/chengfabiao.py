# 打印99 乘法表
for i in range(1, 10):
    s = ''
    for j in range(1, i + 1):
        s += str(j) + '*' + str(i) + '=' + str(i * j) + ' '
    print(s)
    print()
