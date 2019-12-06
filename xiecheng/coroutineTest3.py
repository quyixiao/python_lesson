def counter(n):
    for x in range(n):
        yield x


def inc(n):
    yield from counter(n)


# yield from iterable 是for item in iterable : yield item 形式的语法糖


foo = inc(10)
print(next(foo))
print(next(foo))

