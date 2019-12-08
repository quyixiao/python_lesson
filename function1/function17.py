#
def sort(iterable, reverse=False, key=lambda x, y: x < y):
    ret = []
    for x in iterable:  # 拿出元素
        for i, y in enumerate(ret):
            flag = key(x, y) if not reverse else not key(x, y)
            if flag:
                ret.insert(i, x)
                break
        else:
            ret.append(x)
    return ret


print(sort([1, 2, 3, 4, 5, 6, 7, 8], True, key=lambda x, y: x < y))
# 排序问题，自定义函数，sort 函数的实现，下面的实现是什么排序，如果是reversed
#
# sorted （iterable[,key],[,reverse]）排序
# 返回一个新的列表，对一个可迭代对象的所有元素进行排序，排序的规则为key 定义的函数，reverse表示是否排序翻转
# sorted(lst,key=lambda x : 6 - x )
# filter(function,iterable)
#


