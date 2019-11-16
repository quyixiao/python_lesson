a = 1
sum = 0
max = 10
for i in range(1, max):
    b = 1
    for j in range(1, i + 1):
        b = j * b
    print('==========================' + str(i) + " ------------" + str(b))
    sum += b
print(sum)



######
