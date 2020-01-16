# 将购物车改告成，
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


    def __add__(self, other):
        self.items.append(other)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items.insert(index,value)


cart = Cart()

print(len(cart))
cart.additem(1)
cart.additem(2)
cart.additem(3)
print(len(cart))
print('--------------------------')
for x in cart:
    print(x )

print(1 in cart)
print(cart[2])

print('+++++++++++++++++++++++++++++++++')