
f = open('test','r+')
print(f.read().encode())
f.seek(0)

print(f.readline(1)) # readline 传参1

print(f.readline(1))
print(f.readline(1))
print(f.readline(1))
print(f.readline(1))
print(f.readline(1))
print(f.readline(1))
f.close()