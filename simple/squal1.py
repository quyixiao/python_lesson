a = int(input(">>>"))
i = 0
while i <= (a - 1):
    if i == 0 or i == (a - 1):
        print("*" * a);
    else:
        print("*" + " " * (a - 2) + "*")
    i += 1
