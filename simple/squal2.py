number = int(input("please input a number "))

print("*" * number)

for i in range(number - 2):
    for j in range(number):
        if j == 0 or j == number:
            print("*" + " " * (number - 2) + "*")
else:
    print("*" * number)
