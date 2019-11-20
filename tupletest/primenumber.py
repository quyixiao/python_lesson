import datetime

n = 100
primenumber = []
for x in range(2,n):
    for i in primenumber :
        if x % i == 0 :
            break
    else :
        primenumber.append(x )

print(primenumber)

print('==================================================')


start = datetime.datetime.now()



upper_limit = 10000
x = 5
step = 2
count = 2
while x < upper_limit :
    for i in range(3,int(x ** 0.5) + 1 ,2 ):
        if not x % i :
            break
    else:
        count +1
    x += step
    step = 4 if step == 2 else 2


delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
