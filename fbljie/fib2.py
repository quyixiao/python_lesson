
max1 = 10

def fib(n):
    a =  1 if n < 2 else fib(n - 1) + fib(n - 2)
    print(a)
    return a


fib(10)