import pickle


# 对于一个对象来说，会将对象的属性保存起来
# 对于方法而言，没有将这些属性保存起来
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
