a = 1, 2, 3

print(type(a))

print(a)
# 解构
x, y = 1, 2  # 等号右边使用了封装，而左边就使用解构

print(x)
print(y)

# 封装 和解构
# 封装
# 将多个值使用逗号分割，组合成一起
#  本质上，返回一个元组，只是省掉了小括号
# python 特有的语法，被很多的语言借签
t1 = (1, 2)
t2 = 1, 2  # 将1 和 2 封装成元组
print(type(t1))
print(type(t2))

# 解构
# 把线性结构的元素解开，并顺序的赋值给其它变量

# x, y = 1, 2, 3, 4 要求两边的个数必须是一致的，如果两边的结构是不一致的，那么直接导致问题
x, y = list((2, 3))

print('===============' + str(x))
print(y)
x, y = 'ab'

print(x)
print(y)

a, b = 1, 2
a, b = (1, 2)
a, b = [1, 3]
a, b = [10, 20]
print(a)
a, b = {10, 20}
print(a, b)
a, b = {'a': 10, 'b': 20}
print(a, b)

# a,b = {1,2,3} 个数不匹配

print(a, b)
a, *b = {10, 20, 30}  # * 在python 中的用法很多
print(a, b)

[a, b] = (100, 200)
print(a, b)

# * 使用变量名 接收，但是不能单独使用
# 被*变量名收集后的 ,* 表示尽可能多的吞噬掉多的东西
lst = list(range(1, 101, 2))
head, *mid, tail = lst
print(head, mid, tail)
head, *mid, tail = (1, 2)
print(head, mid, tail)

#
