sun = int (input (''))
num = 1
while True :
    a = input('')
    if not a :
        break
    sun += int(a)
    num += 1
print(str(sun)+ '/ ' + str(num )+ '=' + str(sun / num))
