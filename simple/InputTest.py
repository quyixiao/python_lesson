n = int(input("input the square's length >>>"))
sepTop= "*"
sepMid = "*"
for i in range(0,n):
    sepTop += "\t*"
    sepMid += "\t"
else:
    sepMid +="*"
    print(sepTop)
for i in range(0,n-1):
    print("\n")
    print(sepMid)
else:
    print("\n")
    print(sepTop)
