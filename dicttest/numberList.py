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

strs = 'abcdefghijklmnopqrstuvwxyz'

dict1 = {}
for i in range(10000):
    str1 = ''.join(random.sample(strs, 2))
    if str1 not in dict1:
        dict1[str1] = 1
    else:
        dict1[str1] += 1
for j in reversed(sorted(dict1.keys())):
    print(j, end=' ')
    print('Repeat {} times '.format(dict1[j]))

# 生成数据的过程和处理数据的情况怎样






