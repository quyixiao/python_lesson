encoding = 'utf-8'

chars = set(""",.[]()-+/\*&%#$@` \r\n""")


def makekey2(key):
    start = 0
    # 写你的逻辑，多个元素list
    for i, c in enumerate(key):
        if c in chars:
            if start == i:  # 特殊符号挨着的问题
                start = i + 1
                continue
            yield key[start:i]
            start = i + 1
    else:
        if start < len(key):
            yield key[start:]


def wordcount(filename):
    """ 
    这个函数进行参数迭代，后面返回
    """
    d = {}
    with open(filename, encoding='utf-8') as f:
        for line in f:
            for word in map(str.lower, makekey2(line)):
                d[word] = d.get(word, 0) + 1
    return d

def top(d: dict, n: int = 10): # 这个地方迭代出top 数据 一般来说，我们要进行数据进行直接加工，这个是测试代码，元组这个地方加不加，
    for i, (k, v) in enumerate(sorted(d.items(), key=lambda item: item[1], reverse=True)):
        if i >= n:
            break
        print(k, v)


d = wordcount('sample')
top(d, 50)
