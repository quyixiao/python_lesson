
class Person:
    """hello"""
    age = 3
    def __init__(self,name):
        self.name = name

print('-----------class------------------')
print(1,Person.__class__)
print(2,sorted(Person.__dict__.items()))


tom = Person('tom')
print(3,tom.__class__)
print(4,tom.__dict__)

# 类属性是保存在类中，实例属性是保存在实例中，


print(5,tom.__class__.__dict__)
print(6,sorted(tom.__class__.__dict__.items()))