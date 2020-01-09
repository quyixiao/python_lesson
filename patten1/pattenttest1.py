#\d{3}(?!\d) 匹配，断言3位数字后面的一定不能有数字
# 正则表达式
# 不要在表达式中加入注释
# 断言不占分组号，断言如同条件，只是要求匹配必须满足断言的条件
# 分组和捕获是同一个意思
# 使用正则表达式，能用简单表达式，就不要复杂的表达式
# 默念是贪婪模式，也就是尽量的多匹配更长字符串
# 匹配单词的边界，\bb在文本中找到单词的中的b开头的字母
# \B 不匹配单词边界，
# Python 使用了 re模块提供了正则表达式处理能力
# re.M
# re.MULTILINE 多行模式
# re.S
# re.compile(pattern,flags=0)
# 设定 flags ，编译模式，返回表达式的对象的正则对象 regex
# pattern 就是正则表达式，就不需要再次编译了
# re 的其他方法是为了提高效率都调用了编译方法，就是为了提速
#
import  re
s = '''bottle\nbag\nbig\napple'''
for i ,c in enumerate(s,1):
    print((i -1 ,c),end = '\n' if i % 8 == 0 else ' ')

print()
print(re.match('bo',s))
print(re.match('bott',s)) # 从头开始，有就有，没有就没有

regex = re.compile('bag',s)



print(regex.match(s,8))





