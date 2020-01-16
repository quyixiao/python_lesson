# 方法 意义
# __len__ 内建函数len() ，返回对象的长度(>= 的整数) , 如果把对象当做容器类型来看，就如同 或者 dict，bool()函数调用的时候，如果没有
# __bool__()方法，则会看到__len__()，方法是否存在，存在返回非为真
# __iter__ 迭代容器时，调用返回一个新的迭代器对象
# __contains__ in 成员运算符，没有实现，就调用__iter__方法遍历
# __getitem__  实现self[key] 访问，序列化对象，key 的亲爱整数为索引，或者切片，
class A (list):
    def __missing__(self, key):
        print('miss key = {} '.format(key))
        return 0

a = A()
a.append(2,3,4,5)
a[1 ] = 1
a[3] = 3
print(a[2])








