pre = 0
cur = 1
print(cur, end=' ')


# 改进
# 左边的fib函数和循环的思想是类似的
# 参数n是边界条件，用n 来计数
# 上一次的计算结果直接作为函数的实参
# 效率很高
# 和循环相比，性能相近，所以并不是递归就是好的，存在递归的问题
# 

def fib(n, pre=0, cur=1):
    pre, cur = cur, pre + cur
    print(cur, end=' ')
    if n == 2:
        return
    fib(n - 1, pre, cur)


fib(10)
