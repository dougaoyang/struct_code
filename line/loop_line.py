class Node:
    def __init__(self, elem, next=None, prev=None):
        self.elem = elem
        self.next = next
        self.prev = next


class LoopLine:
    """循环链表"""

    def __init__(self):
        self._head = None
        self._rear = None
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

        if self.is_empty():
            self.append(elem)
        else:
            if index == 0:
                node.next = self._head
                node.next.prev = node
                self._head = node
                self._length += 1
            elif index == self.length():
                self.append(elem)
            else:
                pre = self._head
                i = 0
                while pre.next is not None and i < index-1:
                    pre = pre.next
                    i += 1

                node.prev = pre
                node.next = pre.next
                pre.next.prev = node
                pre.next = node
                self._length += 1

    def append(self, elem):
        node = Node(elem)
        if self.is_empty():
            self._head = node
            self._rear = node
        else:
            self._rear.next = node
            node.prev = self._rear
            self._rear = node
        
        self._length += 1

    def delete(self, index):
        if self.is_empty():
            raise ValueError

        if index < 0 or index > self.length():
            raise ValueError

        if index == 0:
            self._head = self._head.next
            self._head.prev = None
        elif index == self._length - 1:
            self._rear = self._rear.prev
            self._rear.next = None
        else:
            curr = self._head
            i = 0
            while i < index:
                curr = curr.next
                i += 1
            
            pre = curr.prev
            pre.next = curr.next
            pre.next.prev = pre

        self._length -= 1

    def travel(self, reverse=False):
        if not reverse:
            curr = self._head
            while curr is not None:
                yield curr.elem
                curr = curr.next
        else:
            curr = self._rear
            while curr is not None:
                yield curr.elem
                curr = curr.prev

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

    ll = LoopLine()

    ll.append(0)
    ll.append(1)
    ll.append(2)
    print(list(ll.travel()))
    print(list(ll.travel(reverse=True)))

    ll.insert(0, 111)
    print(list(ll.travel()))
    ll.insert(1, 222)
    print(list(ll.travel()))
    ll.insert(6, 333)
    print(list(ll.travel()))
    print(list(ll.travel(reverse=True)))

    ll.delete(0)
    print(list(ll.travel()))
    print(list(ll.travel(reverse=True)))
    ll.delete(4)
    print(list(ll.travel()))
    print(list(ll.travel(reverse=True)))
    ll.delete(1)
    print(list(ll.travel()))
    print(list(ll.travel(reverse=True)))

    print(ll.length())
