# 将购物车改告成，
# python 运算符的重载比 java 要牛逼得多

class Cart:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)


    def __iter__(self):
        #yield  from self.items
        return iter(self.items)

    def additem(self,item):
        self.items.append(item)
        return self

    def __add__(self, other):
        self.items.append(other)
        return self

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items.insert(index,value)

    def __str__(self):
        return "{}".format(self.items)

cart = Cart()
print(len(cart))
cart.additem(1)
cart.additem(2)
cart.additem(3)
cart.additem('abc')
print(len(cart))
print('--------------------------')
for x in cart:
    print(x )

print(1 in cart)
print(cart[2])

print('+++++++++++++++++++++++++++++++++')
print(cart)

cart + 100 + 200 + 300 + 400
print(cart)
cart.additem(900).additem(300).additem(200)
print(cart)

