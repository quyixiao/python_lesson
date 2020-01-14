class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 如果是下划线开头的属性，我们称为私有属性

    def showage(self):
        print(self.__age)

    def grouwup(self, i=1):
        if 0 < i < 100:
            self.__age += 1
        else:
            raise Exception()


tom = Person('tom', 20)
tom.name = 'jerry'
print(tom.name)
tom.showage()
# print(tom.age)
tom.__age = 20000  #
print('-------------------', tom.__age)
print(tom.showage())  #
print(tom.__dict__)  # {'name': 'jerry', '_Person__age': 20, '__age': 20000} , _Person__age 私有属性是在类的定义中
tom._Person__age = 3000 # 在 python 中，在字典中是可以修改的，python 的隐患极大
tom.showage()
# 新的名称，也没有东西是
#

