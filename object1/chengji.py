import bisect
# 特殊属性
# 属性 含义
# __name__ 类，函数，方法等名字
# __module__，类定义所有的
# __class_ 对象或类的所有属性
# __bases__ 类的基类的元组，顺序为它们在基类列表列表中出现的顺序
# __doc__，类的函数文档字符串，如果没有定义则为 None
# __mro__,类的 mro，class.mro()返回结果的保存在__mro__中
# __dic__,类或实例的属性，可写的字典
#
breakpoint = [60, 70, 80, 90]
grades = "EDCBA"
score = 55
a = bisect.bisect(breakpoint, score)
print(a, grades[a])


def get_grade(score, breakpoint=[60, 70, 80, 90], grades="EDCBA"):
    return grades[bisect.bisect(breakpoint, score)]


get_grade1 = lambda score, breakpoint=[60, 70, 80, 90], grades="EDCBA": grades[bisect.bisect(breakpoint, score)]


print(get_grade(55))


print(get_grade1(55))

#
print(get_grade1.__name__,get_grade1.__module__)
print(get_grade.__name__,get_grade.__module__)

print(get_grade.__dir__())
print(dir(get_grade))


if __name__ == '__main__':
    pass




