
# 注意__init__()方法不能有返回值，也就是只能有 None
# 实例对象，instance
# 类的实例化一定会获得 一个对象，就是实例对象，
# 上例中的 tom,jerry 就是 person 类的实例
# __init__方法的第一个参数 self 就是指一批


class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def showage(self):
        print('{} is {} '.format(self.name,self.age))



tom = Person('tom',19)
jerry = Person('jerry',20)

tom.showage()
jerry.showage()


print(id(tom.showage()))
print(id(jerry.showage()))


jerry.age += 2

jerry.name += '893283892'
print(jerry.showage())