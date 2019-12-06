def counter():
    i = 0
    while True:
        i += 1
        yield i


def inc(c):
    return next(c)


c = counter()
print(inc(c))
print(inc(c)) # 这个执行的结果，


