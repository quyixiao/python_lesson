def counter():
    #c = 5
    c = [5]
    def inner():
        # c = c + 5 #
        #c.add(6)
        c.append(6)
        return c
    return inner

foo = counter()
print(foo(), foo())



print(foo())