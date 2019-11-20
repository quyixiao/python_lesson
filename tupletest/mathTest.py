import datetime
import math

#如果一个数能被素数整除，就是一个合数

start = datetime.datetime.now();
count = 1
primenumber = []
flag = False
upper_limit = 100
for x in range(3, upper_limit, 2):
    up = math.ceil(math.sqrt(x))
    for i in primenumber:
        if x % i == 0:
            flag = True
            break
        if i >= up:
            flag = False
            break
    if not flag:
        primenumber.append(x)
        count += 1
print(count)
end = (datetime.datetime.now() - start).total_seconds()
print(primenumber)



