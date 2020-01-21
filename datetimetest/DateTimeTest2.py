g = ["{:04}".format(i) for i in range(1, 11)]
for x in g:
    print(x)
print('-----------------------------------')
for x in g:
    print(x)

# 总结
# 立即计算，返回的不是迭代嘎嘎，返回的是可迭代对象
# 从前往后走一遍后，可以重新回到迭代

#{[x] for x in range(5)}

#print({{x} for x in range(5)})

# 集合解析式
#print({{x,x+1} for x in range(5)}) #  语法
# { 返回值 for 元素 in 可迭代对象 if 条件}
# 列表解析式中的括号换成大括号{} 就行了
# 立即返回一个集合

print({(x,x + 1) for x in range(10)})

# 这个是一个错误的
#print({[x] for x in range(20)})idie

#print({(x,[2]) for x in range(10)}) 这个也是错误的


#  字典




