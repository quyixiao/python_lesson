n = 12577
flag = False
for i in range(2, n):
    if n % i == 0:  # 找到条件是什么
        flag = True
        print(i)
        break
if flag:
    print(n, 'is not a print ')
else:
    print(n, 'is a prime number .')

###################################################
n = 12577
flag = False
for i in range(2, n):
    if n % i == 0:
        print(n, 'is not a prime number .')
        break
else:
    print(n, 'is a prime number .')
