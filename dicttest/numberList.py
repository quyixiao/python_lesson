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


# 按照什么东西排序 ，按照key 来进行排序
f = sorted({'a': 1, 'c': 2, 'd': 5, 'b': [1, 2, 3]}.items(), key=str)

print(f)

words = []
for _ in range(100):
    # words.append(random.choice(strs) + random.choice(strs))
    # words.append(''.join(random.sample(strs,2)))
    words.append(''.join(random.choice(strs) for _ in range(2))) # 生成器

print(words)