# 用面向对象的列表
# 结点

class SingleNode:
    """结点类"""

    def __init__(self, item, next=None, prev=None):
        self.item = item
        self.next = next
        self.prev = prev

    def __repr__(self):
        return "{} ==> {} ==> {}".format(
            self.prev.item if self.prev else None,
            self.item,
            self.next.item if self.next else None)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.items = []

    def append(self, item):
        """尾部追加"""
        node = SingleNode(item)
        tail = self.tail
        # 当前的尾部是谁
        # 当前的尾部的下一个指向新的 node
        # node 将为 tail
        if tail is None:  # 如果是第一个元素
            self.head = node
        else:
            tail.next = node  # 当前尾部的下一个指向新的node
            node.prev = tail
        self.tail = node
        self.items.append(node)
        return self

    def pop(self):
        """实现尾部弹出"""
        # empty
        if self.tail is None:
            raise Exception('empty')

        # just one
        # if self.head is self.tail:
        # if self.tail.pre is None:
        node = self.tail
        if self.head.next is None:
            self.head = None
            self.tail = None
            # >
        else:
            node.prev.next = None
            self.tail = node.prev

        self.items.pop()
        return node

    def insert(self, index, item):
        if index < 0:
            raise IndexError('Wrong index {} '.format(index))

        current = None
        for i, node in enumerate(self.iternodes()):
            if i == index:
                current = node
                break
        else:  # 超出当前迭代 index > length - 1
            self.append(item)
            return
        node = SingleNode(item)
        prev = current.prev
        if index == 0:
            node.next = current
            current.prev = node
            self.head = node
        else:
            prev.next = node
            current.prev = node
            node.next = current
            node.prev = prev

        self.items.insert(index, node)

    def remove(self, index):
        if index < 0:
            raise IndexError('Wrong index {} '.format(index))

        if self.tail is None:
            raise Exception('没有元素')

        # just one
        # if self.head is self.tail:
        # if self.tail.pre is None:  当只有一个元素的时候
        if self.head.next is None:
            node = self.head
            self.head = None
            self.tail = None
            return 0

        current = None
        for i, node in enumerate(self.iternodes()):
            if index == i:
                current = node
                break
        else:
            self.pop()
            self.items.pop()
            return index

        prev = current.prev
        next = current.next
        if index == 0:
            next.prev = None
            self.head = next
        elif next is None:
            # tail 处理
            prev.next = None
            self.tail = prev
        else:
            # mid 处理
            prev.next = next
            next.prev = prev
        del current

        self.items.pop(index)
        return index

    def iternodes(self, reverse=False):
        current = self.tail if reverse else self.head
        while current:
            yield current
            current = current.prev if reverse else current.next


ll = LinkedList()
ll.append('abc').append('def').append('111111').append('2222222').append('333333').append('4444444')
ll.insert(2, 'xxx')
ll.insert(1000, 'yyyy')
for x in ll.iternodes():
    print(x)
print('------------------------')
ll.remove(0)
for x in ll.iternodes():
    print(x)

# print(ll.pop())
# print(ll.pop())
# print('------------------------')
# for x in ll.iternodes():
#     print(x)
