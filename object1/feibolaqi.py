# 定义一个斐波那契列的类，方便调用，计算第 n 项
class Fib:
    def __init__(self):
        self.items = [0, 1, 1]

    def __len__(self):
        return len(self.items)

    def __call__(self, *args, **kwargs):
        l = len(self.items)
        if l <= args[0]:
            for i in range(l, args[0] + 1):
                x = self.items[i - 1] + self.items[i - 2]
                self.items.append(x)
        return self[args[0]]

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

fib = Fib()
print(fib(10))
print(fib(11))
print('---------------------')
for x in range(20):
    print(fib(x))

print('---------------------')
for x in fib:
    print(x)
print('------------------------------------')
print(fib[10])












