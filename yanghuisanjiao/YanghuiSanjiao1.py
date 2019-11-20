n = 6
pre = [1]
print(pre)
pre.insert(0, 0)
pre.append(0)
for i in range(1, n):                   #只是向前移动了一们而已的
    newline = []
    for j in range(i + 1):
        val = pre[j] + pre[j + 1]
        newline.append(val)
    print(newline)
    pre = newline
    pre.insert(0, 0)
    pre.append(0)
