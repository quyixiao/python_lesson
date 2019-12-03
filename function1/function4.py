# global 解决闭包问题
def counter():
    global c

    def inner():
        global c
        c = 10
        return c + 1

    return inner


foo = counter()
print(foo(), foo())
print(foo())
