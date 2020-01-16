class A :
    def __init__(self,name = 'tom',age=18):
        self.name = name
        self.age = age

    def __hash__(self):
        return 1

    def __repr__(self):
        return "<A name={} ,age={}>".format(self.name,self.age)



# 每一次都是一样的
# print(hash(A))
# print(hash(A))
#
# print(hash(A('zhangsan',10)))
# print(hash(A('lisi',20)))

item = [A(),A()]
print(item)

item = (A(),A())

print(item)

item = {A(),A('jerry')}

print(item)


# hash 只是计算has 上 值的问题，解决的是存在什么地方，hash 的
# 去重，用到 hash
#








