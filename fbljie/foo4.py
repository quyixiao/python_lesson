# 但是，如果构成了循环的递归调用是非常的危险的，但是往往这种情况下代码的复杂情况下，还是可能发生这种调用的，要用代码的规范来避免这种问题
# 这种递归调用发生了
# 递归是一种很自然的
# 即使递归代码是非常的简单的，但是能不用的情况下，最好是不要使用
# 绝大的多数的递归，都可以使用循环来实现
# 如果是限制次数的递归，可以使用递归调用，或者使用循环代替，循环代码稍微的复杂一些，但是只要不是死循环，可以多次迭代的使用递归
# 求n 阶乘
# 将一个放入到列表中，1234 [4,3,2,1]
#

def njiecheng(n):
    if n < 2:
        return 1
    return n * njiecheng(n - 1)


print(njiecheng(5))


def factorial(n, mul=1):
    mul *= n
    if n == 1:
        return mul
    return factorial(n - 1, mul)


print(factorial(5))


def nreversed(a, n):
    if a is None:
        a = []
    if n < 10:
        a.append(n)
    else:
        b = n % 10
        a.append(b)
        n = n // 10
        a = nreversed(a, n)
    return a


a = nreversed([], 123456789)
print(a)
