import pickle

x = 'a'
y = 100
z = ['a', 'b', 'c']
m = {'x': x, 'y': y, 'z': z}
filename = '/Users/quyixiao/ttg/qqq'

# 序列化数据
with open(filename, 'wb') as f:
    n = pickle.dumps(m)
    print(n,type(n))

# 反序列化数据
with open(filename, 'rb') as f:
    for _ in range(1):
        a = pickle.loads(n)
        print(a, type(a))
        print(a.keys()) # 如果知道原来的类型，每个数据的类型，如果不知道数据的边界，






