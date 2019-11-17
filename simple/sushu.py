import datetime

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

###################################
start = datetime.datetime.now()
count = 0
for x in range(2, 200000):
    flag = True
    for y in range(2, int(x ** 0.5) + 1):
        if x % y == 0:
            flag = False
            break
    if flag:
        count += 1

print(count)
end = (datetime.datetime.now() - start).total_seconds()
print(end)