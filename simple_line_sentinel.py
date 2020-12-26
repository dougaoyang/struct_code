# 使用哨兵结点处理结点的边界问题
import math


class Node:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next


class SimpleLine:

    def __init__(self):
        sentinel = Node(None)
        self._head = sentinel # 添加哨兵结点
        self._length = 0

    def get_head(self):
        return self._head.next

    def append(self, elem):
        node = Node(elem)

        curr = self._head
        while curr.next is not None:
            curr = curr.next
        curr.next = node

        self._length += 1

    def insert(self, index, elem):
        if index < 0 or index > self._length:
            raise ValueError

        node = Node(elem)
        pre = self._head
        i = 0
        while i < index:
            pre = pre.next
            i += 1

        node.next = pre.next
        pre.next = node

        self._length += 1

    def pop(self):
        if not self._length:
            raise ValueError

        pre = self._head
        while pre.next.next is not None:
            pre = pre.next

        node = pre.next
        pre.next = None

        self._length -= 1
        return node.elem

    def delete(self, index):
        if not self._length:
            raise ValueError

        if index < 0 or index > self._length - 1:
            raise ValueError

        pre = self._head
        i = 0
        while i < index:
            pre = pre.next
            i += 1

        node = pre.next
        pre.next = pre.next.next
        self._length -= 1
        return node.elem

    def travel(self):
        curr = self._head.next
        while curr is not None:
            yield curr.elem
            curr = curr.next

    def reverse(self):
        """返回一个新链表"""
        new = SimpleLine()
        curr = self._head.next
        while curr is not None:
            new.insert(0, curr.elem)
            curr = curr.next
        return new

    def reverse2(self):
        """原地修改"""
        if self._length <= 1:
            return

        pre = self._head.next # 待反转结点的上一个结点
        curr = self._head.next.next # 待反转的结点
        
        while curr is not None:
            pre.next = curr.next
            curr.next = self._head.next
            self._head.next = curr
            curr = pre.next

    def check_loop(self):
        """链表中环的检测, 快慢指针"""
        if self._head is None:
            return False

        p1 = self._head.next # 慢结点
        p2 = self._head.next  # 快结点

        while (p1 is not None) and (p2 is not None )and (p2.next is not None):
            p1 = p1.next
            p2 = p2.next.next

            if p1 == p2:
                return True

        return False

    def middle_node(self):
        """中间结点(长度取半)"""
        if self._head.next is None:
            return None

        middle = math.floor(self._length / 2)
        curr = self._head.next
        i = 0
        while i < middle:
            curr = curr.next
            i += 1
        return curr.elem

    def middle_node2(self):
        """中间结点(快慢指针)"""
        if self._head.next is None:
            return None

        p1 = self._head.next  # 慢结点
        p2 = self._head.next  # 快结点

        while (p2 is not None) and (p2.next is not None):
            p1 = p1.next
            p2 = p2.next.next
        return p1.elem


if __name__ == '__main__':

    sl = SimpleLine()

    sl.append(1)
    sl.append(2)
    sl.append(3)
    sl.append(4)
    sl.append(5)
    sl.append(6)
    sl.append(7)
    sl.append(8)
    print(list(sl.travel()))

    # sl2 = sl.reverse()
    # print(list(sl2.travel()))

    # sl.reverse2()
    # print(list(sl.travel()))

    # print(sl.check_loop())
    print(sl.middle_node())


