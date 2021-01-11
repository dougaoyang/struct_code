class Node:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next


class SimpleLine:
    """链表实现线性表"""

    def __init__(self):
        self._head = None
        self._length = 0

    def is_empty(self):
        return self._head == None
    
    def clear(self):
        self._head = None
    
    def getElem(self, index):
        if index < 0 or index > self.length():
            raise ValueError

        curr = self._head
        i = 0
        while i < index:
            curr = curr.next
            i += 1

        return curr.elem
    
    def locateElem(self, elem):
        curr = self._head

        index = -1
        i = 0
        while curr is not None:
            if curr.elem == elem:
                return i
            curr = curr.next
            i += 1
        return index

    def insert(self, index, elem):
        if index < 0 or index > self.length():
            raise ValueError

        node = Node(elem)

        if index == 0:
            node.next = self._head
            self._head = node
        else:
            pre = self._head
            i = 0
            while i < index-1:
                pre = pre.next
                i += 1

            node.next = pre.next
            pre.next = node

        self._length += 1

    def append(self, elem):
        node = Node(elem)
        if self.is_empty():
            self._head = node
        else:
            curr = self._head
            while curr.next is not None:
                curr = curr.next
            curr.next = node

        self._length += 1

    def delete(self, index):
        if self.is_empty():
            raise ValueError

        if index < 0 or index > self.length():
            raise ValueError

        if index == 0:
            self._head = self._head.next
        else:
            pre = self._head
            i = 0
            while i < index-1:
                pre = pre.next
                i += 1

            pre.next = pre.next.next

        self._length -= 1

    def travel(self):
        curr = self._head
        while curr is not None:
            yield curr.elem
            curr = curr.next

    def length(self):
        return self._length

    def length_old(self):
        curr = self._head
        count = 0
        while curr is not None:
            curr = curr.next
            count += 1
        return count


if __name__ == '__main__':
    sl = SimpleLine()

    sl.append(0)
    sl.append(1)
    sl.append(2)
    print(list(sl.travel()))

    sl.insert(3, 111)
    sl.insert(3, 222)
    print(list(sl.travel()))

    print(sl.getElem(2))

    print(sl.locateElem(222))

    sl.delete(4)
    print(list(sl.travel()))

