
def counter():

    c = 10
    def inner():
        global c
        c = 10
        return c + 1

    return inner


foo = counter()

print(foo(), foo())

print(foo())
