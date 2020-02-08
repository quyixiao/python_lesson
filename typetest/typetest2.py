class A:
    a =1000


print(type(dict))
print(type({}))
print(type(type))
print('----------------------------')
print(A)
print(type(A))
print(A.__dict__)
print('*'*30)

def __init__(self):
    self.x = 1000
    print('B.init........')

def show(self):
    print('--------------------',self.__dict__)
    print(self.b)

B = type('C_B', (), {'b':2000,'__init__':__init__,'show':show})

print(B)
print(type(B))
print(B.mro())
print(B.__dict__)


b = B()
b.show()

