for i in range(1, 10):
    line = ''
    for j in range(1, i + 1):
        line += '{}*{}={:<5}'.format(j, i, i * j)  # 表示占位符
    print(line)

print("=====================================")

for i in range(1, 10):
    line = ''
    for j in range(i, 10):
        line += '{}*{}={:<4}'.format(i, j, i * j)  # 表示占位符
    print('\t' * (i - 1) * 2 + line)

print("=====================================")

withd = 0
for i in range(1, 10):
    line = ''
    for j in range(i, 10):
        line += '{}*{}={:<{}}'.format(i, j, i * j, 3 if j < 4 else 4)  # 表示占位符
        withd = max(withd, len(line))
    print("{:>{}}".format(line, withd))

print("=====================================")

withd = 0
for i in range(1, 10):
    line = ''
    for j in range(i, 10):
        line += '%d*%d=%2d ' % (i, j, j * i)  # 表示占位符
        withd = max(withd, len(line))
    print("{:>{}}".format(line, withd))

print("=====================================")

print(3, 3, sep='&', end='    ')
