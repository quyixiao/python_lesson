print((i for i in range(5)))  # <generator object <genexpr> at 0x10d8c71d0> 生成器对象表达式

print([i for i in range(5)])  # [0, 1, 2, 3, 4] 生成一个列表

g = (i for i in range(5))

print(g)

for iii in g:
    print(iii)

# () 这个是你找要一个，我就生成一个，如果你不找我要，那么，我也不再生成一个对象
# () 生成器表达式，生成器表达式，生成器对象，range()返回一个对象，如果要元素，就生成一个，[] 即使你不要，我也生成这个对象
# () 这个东西名字叫做惰性求值，
# 语法
# (返回值 for 元素 in 可迭代对象中 if 条件)
# 列表解析式的中括号换成小括号就行了
# 返回一个生成器
# 和列表解析式的区别
# 生成器表达式
# 如果我们知道这个这个东西，如果立即返回一个对象，惰性求值，立即计算，什么时候用。
# python 惰性求值，很多的函数都是惰性的，如果我要用的时候，才进行计算，如果计算量不是很多的，什么时候需要的，就什么时候提前使用，
# 生成器
#


print('===============================')

g = (i ** 0.5 for i in range(5))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# 和列表解析式的对比
# 计算方式，
# 生成器表达式延迟计算，列表解析式立即计算
# 列表解构式需要占用的内存


print((x,) for x in range(10))
#
print({x, (x, [1])} for x in range(10))

print(id([1]) == id([1]))
# 这两个值是不一样的，但是，我觉得这个还是好的，
print(id([1]))
print(id([1]))
# 拿到这个东西已后，判断他们相不相等，比较内容，内容一致，肯定东西是一样的。

#
print([1] is [1])  # return false
# 哈希
#  返回一个对象的哈希值
#
print(type(1))
print(type(type(1)))  # 是一个 type类型
# 类型转换
#  float ,int ,bin ,hex oct ,bool list tuple ,dict ,set complex,bytes ,bytearray()
# input([prompt])
# 打印 print(*objects,sep='',end ='\n')


# 对象长度
# len ()表示类型的长度，用于集合类型
# isinstance(object,class or tuple)
# 判断对象 obj 是否属于某种类型或者
#
print(isinstance('abc', (int, float, str)))

print(issubclass(bool, str))  # 一个 bool 类型不是 str 类型的子类

print(round(-0.51))  # 返回一个值是一个负数
# pow(x,y)
# divmod(x,y) == tuple(x//y,x%y)

x, y = divmod(54321, 10000)
print(x, y)

# 如果看到元组，就可以使用这种方式
# sum(iterable[])
#
print(sum(range(5)))

print(sum(range(5), 2))
print(sum(range(1, 100, 2)))

print(chr(97))

print(chr(20013))

print(ord('中'))

print(hex(ord('中')))

print(repr(1))

print(ascii(1))

print(sorted([1, 5, 2, 3]))
print(sorted([1, 3, 5], reverse=True))
g = reversed(range(5))

print(g)
print(next(g))
print(next(g))
print(next(g))

lst = list(reversed('13579'))
print(lst)
f = {reversed((2, 4))}

for x in reversed(['c', 'b', 'a']):
    print(x)

f = reversed(sorted({1, 3, 5}))

print(f)

# 内建函数
# 迭代器和取元素 iter(iterable),next(iter)
for x in enumerate('abcdef'):
    print(x, end='')

it = reversed([1, 3, 5])
print('------------------------------------')
print(next(it))
print(next(it))
print(next(it))

# 如果报错将给出一个缺省值
# 把一个可迭代的对象作为一个值
#
it = iter(reversed([1, 3, 5]))

print(next(it))

# 如果一个迭代器就直接使用这个值
# 可迭代对象
# 能够通过迭代一次次的返回不同的元素对象
# 所谓相同，不是指
a = [1]
b = [a, a]
print(b)

# 迭代不同对象的元素，相同的元素，相同往往是值相同，不同的元素，是不同的位置上的
#
# 可迭代对象未必是有序的，未必是有序的，但是
# 可以使用成员操作，in ,not in ,in 的本质上就是遍历对象
# in range(10)
# in (x for x in range(10))
# in {x:y for x,y in zip(range(4),range(4,10))}
# 如果线性的东西是 sequence 是不是hash 的值，我觉得，
# 就是因为这些东西写的东西不同，那就使用 zip 函数
# in 是做什么用的，
# 通过 next(g)  方法就可以生成可迭代对象
# 迭代器是不可以回头的
#
f = list(zip(range(10),range(10)))
for x in f :
    print( x )
