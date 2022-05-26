class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self._head = Node

    def is_empty(self):
        return self._head is not None

    def length(self):
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def items(self):
        cur = self._head
        while cur is not None:
            yield cur.item
            cur = cur.next

    def add(self, item):
        # 在头部加入节点
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            # 不是空链表，则找到尾部，将尾部next结点指向新结点
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, index, item):
        if index <= 0:
            self.add(item)
        elif index > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            for i in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        cur = self._head
        pre = None
        while cur is not None:
            # 找到指定元素
            if cur.item == item:
                #
                if not pre:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                return True
            else:
                pre = cur
                cur = cur.next

    def find(self, item):
        return item in self.items()




if __name__ == '__main__':
    link_list = LinkedList()
    node1 = Node(1)
    node2 = Node(2)

    link_list._head = node1
    node1.next = node2

    print(link_list._head.item)
    print(link_list._head.next.item)

    print('link_list.length: {}'.format(link_list.length()))

    for i in link_list.items():
        print(i, end='\t')
    print()
    print('link_list.find(2): {}'.format(link_list.find(2)))