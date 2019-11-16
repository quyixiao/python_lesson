for i in range(1, 10):
    line = ''
    for j in range(1, i + 1):
        line += '{}*{}={:<5}'.format(j, i, i * j)                       #表示占位符
    print(line)
