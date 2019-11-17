list0  = [1,[2,3,4],5]
print(id(list0))
list5 = list0.copy()
print(id(list5))
print(list0)
print(list5)
list0[2] = 10
print(list0)
list0[1][1] = 20
print(list0)
list0[1][0] = 30
print(list5)            #对于
