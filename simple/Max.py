max = 0
count = 1
while True:
    num = int(input('please input a number :'))
    if num > max:
        max = num
    count += 1
    if count > 2:
        choice = input('Continum?(Y/N):')
        if choice == 'N':
            print(max)
            break
################

number = int(input('number'))
n = int(input('how'))
for i in range(n):
    newNumber = int(input('number'))
    if newNumber >= number:
        number = newNumber
else:
    print(number)