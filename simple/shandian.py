num = int(input('num is :'))
mid = num // 2
for i in range(mid, mid - num, -1):
    absi = abs(i)
    if i < 0:
        a = mid
    else:
        a = i
    s = ' ' * a + '*' * (num // 2 + 1 - absi)
    if not i:
        s = '*' * num
    print(s)
