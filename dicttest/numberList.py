import random

numlist = []
for i in range(100):
    numlist.append(random.randint(-50, 50))

numDict = {}

for i in numlist:
    if not numDict.get(i):
        numDict[i] = 1
    else:
        numDict[i] = numDict[i] + 1

listkey = sorted(list(numDict.keys()))

for k in listkey:
    print(k, ' ', numDict[k])
