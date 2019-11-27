lists = [[1, 2, 3, 4], [5, 6, 7, 8]]

wight = len(lists)
height = 0
for i in lists:
    height = len(i)
    for j in i:
        print(j, end=' ')
    print()

print('=========================================')
for i in range(0, height):
    for j in range(0, wight):
        print(lists[j][i], end=' ')
    print()