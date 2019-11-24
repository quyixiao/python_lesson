newline = []
for i in range(6):
    newline.append(i)

newline = [1] * 6

newline = [1 for i in range(6)]  # 这个方法是优化以后的方法

a = print("b")

print(type(a))

list = []
list.append(1)
list.append(2)
print(list)
t = ()
t = tuple(range(1, 2, 7))
print(t)
# 元组只是只读的，所以，增，删除，改，方法都没有的
t = (2, 4, 5, 6, 7)
print(t)
t = (1,)
print(t)
t = (1,) * 5
print(t)
