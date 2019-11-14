n = 5
e = -n // 2
for i in range(e, n + e):
    if i == e or i == n + e - 1:
        print('*' * n)
    else:
        print('*' + ' ' * (n - 2) + '*')
