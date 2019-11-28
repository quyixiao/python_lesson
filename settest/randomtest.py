import random

lst = []
rep_lst = []
uniq_lst = []
for i in range(10):
    tmp = random.randint(1, 20)
    if tmp in lst and tmp not in rep_lst:
        rep_lst.append(tmp)
    lst.append(tmp)

for j in lst:
    if j not in rep_lst:
        uniq_lst.append(j)

print(lst)
print(len(rep_lst), ':', rep_lst)
print(len(uniq_lst), ':', uniq_lst)
