

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