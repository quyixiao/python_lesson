#



d= dict(zip('abcde',range(5)))
key = tuple()
for item in d.items():
    key += item
print(d)
print(key)

key1 = tuple(d.items())
print(key1)