import random

for i in range(0, 10):
    print(random.randint(1, 6), end='\t')

print()

print("===============================")

for i in range(0, 10):
    print(random.randrange(1, 6, 2), end='\t')
print()
print("===============================")

for i in range(0, 10):
    print(random.choice([1, 3, 5, 7]), end='\t')

print()
print("===============================")
list3 = [1, 3, 5, 7, [8, 9, 10]]
random.shuffle(list3)  # 打乱列表的元素

print(list3)

print("===============================")
print(random.sample(['a','b','c','d'],2))
print(random.sample(['a','a'],2))


