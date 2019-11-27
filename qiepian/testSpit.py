import datetime

martrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print('\n method 1 ')
start = datetime.datetime.now()
for c in range(1000000):
    tm = []  # 目标矩阵
    for row in martrix:
        for i, item in enumerate(row):
            if len(tm) < i + 1:
                tm.append([])
            tm[i].append(item)
delata = (datetime.datetime.now() - start).total_seconds()

print(delata)

print("\n method2 ")
start = datetime.datetime.now()
for c in range(1000000):
    tm = [0] * len(martrix[0])
    for i in range(len(tm)):
        tm[i] = [0] * len(martrix)
    for i, row in enumerate(tm):
        for j, col in enumerate(row):
            tm[i][j] = martrix[j][i]

delata = (datetime.datetime.now() - start).total_seconds()
print(delata)
