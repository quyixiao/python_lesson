def counter():
    i = 0
    while True :
        i += 1
        yield i

def inc():
    c = counter()
    return next(c)

print(inc()) # 每次返回的对象都是一样的，
print(inc())
print(inc())
print(inc())


