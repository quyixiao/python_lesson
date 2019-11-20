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
