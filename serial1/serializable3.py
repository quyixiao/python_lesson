import pickle


# 对于一个对象来说，会将对象的属性保存起来
# 对于方法而言，没有将这些属性保存起来
# 如果两边不一致，就会导致各种问题，自己定义的不一致，我们借用了python ，序列化和反序列化可能不一致的
# 这里定义的东西
# 一般来说，本地序列化的情况，应用较少，大多数的场景都应用在网络传输中
# 将数据序列化后通过网络传输到远程节点，远程服务器上的服务将接收到的数据反序列化经后，就可以使用了
# 但是一点是会算注意的一点就是，远程接收端，我们在单位中使用的小项目的时候，
# xml ,Json , {data:{name:1}}，protocol buffer
#
class AAA:
    bbbb = '23898328' # 这个是某个类的
    def __init__(self):
        self.tttt = 'abc'

    def show(self):
        print('ABC')


a1 = AAA()
print(a1.tttt)

filename = 'qqq'

with open(filename, 'wb') as f:
    n = pickle.dumps(a1)
    print(n, type(n))

# 反序列化数据
with open(filename, 'rb') as f:
    for _ in range(1):
        a = pickle.loads(n)
        a.show()
        print(a.tttt)
        print(a.bbbb)
        print(a, type(a))  # 表示是一个对象类型
