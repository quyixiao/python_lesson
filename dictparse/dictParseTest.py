# 语法
# {返回值 for 元素 in 可迭代对象 if 条件}
# 列表解析式中的中括号换成大括号{} 就行了
# 使用 key : value 形式
# 立即返回一个字典
# 用法

print({x: (x, x + 1) for x in range(10)})
print({x: [x, x + 1] for x in range(10)})
print({x: (1, [2]) for x in range(5)})
print({(x,): [x, x + 1] for x in range(10)})
# print({[x]:[x,x + 1 ] for x in range(10)})
print({chr(0x41 + x): x ** 2 for x in range(10)})
print({str(x): y for x in range(3) for y in range(4)})

# 每一种情况要多多的测试
# Python2 引入了列表解析式
# python2.4 引入了生成器表达式
# python3 引入了集合，字典解析式，并迁移到了2.7 上
# 一般来说，应该多应用解析式，简短，高效
# 如果一个解析式非常的复杂，难以读懂，要考虑拆解成 for 循环
# 生成器和迭代器是不同的对象，但是都是可迭代对象

# 但是是可迭代对象



