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