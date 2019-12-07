#
def sort(iterable, key=lambda x, y: x < y):
    ret = []
    for x in iterable:  # 拿出元素
        for i, y in enumerate(ret):
            # flag = True if x > y else False
            if key(x, y):
                ret.insert(i, x)
                break
        else:
            ret.append(x)
    return ret


print(sort([1, 2, 3, 4, 5, 6, 7, 8], key=lambda x, y: x < y))
