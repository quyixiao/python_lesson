#  内存中的字典，列表，集合以用各种对象，如何保存到一个文件中
# 如果是自己定义的类的实例，如何保存到一个文件中
# 如何从文件中读取数据，并让它们在内存中再次变成自己对就的类的实例
# 要设计一套协义，按照某种规则 ，把内存中的数据保存到文件中，文件是一个字节序列，所以必须 氢数据转换成字节序列中，输出到文件中
# 这就是序列化，反之，从文件的字节序列恢复到内存，就是反序列化经
# 如果一个对象存储在内存中，python 能将内存中的数据，保存只是一个顺带的事情，文件存储，是序列化，数据必须转换成一个序列
# 反过来，序列化，
# 序列化保存一以文件吴诗就是持久化
# 可以将数据序列化后持久化，或者网维传输，也可以将从文件中或者网络接收到字节序列化或者反序列化
# python 提供了pickle 库
# python 中的序列化，反序列化模块
# dumps 对象序列化为bytes对象
# dump 对象 没有必要将数字转换成字符串，在内存中的数据一个个的转换成，我们想要的东西，定义一个变量的时候，应该定义成什么类型
# 类型还在，
# m = {'x': x, 'y': y, 'z': z}
import pickle

x = 'a'
y = 100
z = ['a', 'b', 'c']
m = {'x': x, 'y': y, 'z': z}
filename = '/Users/quyixiao/ttg/qqq'

# 序列化数据
with open(filename, 'wb') as f:
    pickle.dump(x, f)
    pickle.dump(y, f)
    pickle.dump(z, f)
    pickle.dump(m, f)

# 反序列化数据
with open(filename, 'rb') as f:
    for _ in range(4):
        a = pickle.load(f)
        print(a, type(a))







