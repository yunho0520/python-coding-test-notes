class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SingleLinkedList1(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return not bool(self.head)

    def add_first(self, item):
        node = Node(item)
        if not self.is_empty():
            node.next = self.head
            self.head = node
        else:
            self.head = node
        self.length += 1

    def add_last(self, item):
        if not self.is_empty():
            node = self.head
            while node.next:
                node = node.next
            node.next = (Node(item))
        else:
            self.head = Node(item)
        self.length += 1

    def insert(self, pos, item):
        if not self.is_empty():
            if pos == 0:
                self.add_first(item)

            elif pos == self.length:
                self.add_last(item)

            else:
                node = self.head
                cnt = 0
                while 0 < pos < self.length:
                    if cnt == pos - 1:
                        new_node = Node(item, node.next)
                        node.next = new_node
                        break
                    node = node.next
                    cnt += 1
                self.length += 1
        else:
            print('list is empty')

    def remove(self, target):
        if not self.is_empty():
            node = self.head
            if node.data == target:
                self.head = node.next
                self.length -= 1
                return True
            else:
                prev = node
                node = node.next
                while node:
                    if node.data == target:
                        prev.next = node.next
                        self.length -= 1
                        return True
                    prev = node
                    node = node.next
                return False
        else:
            print('list is empty')
            return False

    def search_target(self, target):
        if not self.is_empty():
            pos = 0
            node = self.head
            while node:
                if node.data == target:
                    return pos
                node = node.next
                pos += 1
            return False
        else:
            print('list is empty')
            return False

    def search_pos(self, pos):
        if not self.is_empty():
            cnt = 0
            node = self.head
            while node:
                if cnt == pos:
                    return node.data
                node = node.next
                cnt += 1
            return False
        else:
            print('list is empty')
            return False

    def size(self):
        return self.length

    def print(self):
        if not self.is_empty():
            node = self.head
            while node:
                print(node.data, end=' ')
                node = node.next
            print()
        else:
            print('list is empty')
