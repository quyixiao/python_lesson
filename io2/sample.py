encoding = 'utf-8'
d = {}

chars = set(r""",.[]()-+/\*&%#$@`""")

def makekey(x):
    key = x.lower()
    ret = []
    # 写你的逻辑，多个元素list
    for c in key :
        if c in chars:
            ret.append(' ')
        else:
            ret.append(c)
    return "".join(ret).split() # 多个元组的集合

print(makekey('path . os.***path.commongpath(paths)'))

def makekey2(x):
    key = x.lower()
    ret = []
    start = 0
    # 写你的逻辑，多个元素list
    for i,c in enumerate(key) :
        if c in chars:
            if start == i : # 特殊符号挨着的问题
                start = i + 1
                continue
            ret.append(key[start:i])
            start = i + 1
    else :
        if start < len(key):
            ret.append(key[start:])

    return ret # 多个元组的集合

print(makekey2('path . ***os.path.commongpath(paths)'))



with open('sampletest', encoding=encoding) as f:
    for line in f:
        words = line.split()  # path . os.path.commongpath(paths)
        # for word in map(lambda x : x.lower() ,words):
        for wordlist in map(makekey2, words): #如果要对每个元素进行处理，最好使用map 函数，学习函数，还要学习封装。
            for word in wordlist:
                d[word] = d.get(word, 0) + 1

# top 10
print(sorted(d.items(), key=lambda item: item[1], reverse=True))
