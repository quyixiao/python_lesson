import datetime
import functools
import time


@functools.lru_cache()
def add(x, y, z=5):
    time.sleep(z)
    return x + y

start = datetime.datetime.now()
end = datetime.datetime.now()
print('0000000000000000' ,end -start)
print(add(4, 5))
end = datetime.datetime.now()
print('11111111111111',end -start)
print(add(4, 5))
end = datetime.datetime.now()

print('101001010',end -start)
print(add(4.0, 5))
end = datetime.datetime.now()
print('22222222',end -start)

print(add(4, 6))
end = datetime.datetime.now()
print('3333333333',end -start)

print(add(y=6, x=4))
end = datetime.datetime.now()
print('444444444444',end -start)


print(add(x=4 ,y=6))
end = datetime.datetime.now()
print('5555555555',end -start)
