# 打印菱形
line = int(input('>>>>'))
for i in range(-line // 2, line // 2 + 1):
    if i < 0:
        print(' ' * (-i) + '*' * (line + 2 * i))
    if i >= 0:
        print(' ' * i + '*' * (line - 2 * i))

print('=======================')
for i in range(-line // 2, line // 2 + 1):
    if i < 0:
        print(' ' * (-i) + '*' * (line + 2 * i))
    else:
        print(' ' * i + '*' * (line - 2 * i))


print('==========================')
print(max(1,2,3,4,5,6,7,8,9,10))

