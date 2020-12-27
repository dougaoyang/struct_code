# 使用数组队列实现循环队列
"""
0 1 2 3 4 0 1 2 3 4
当head==tail队列为空
当 (tail + 1)%len = head队列已满
len=5
tail=3; head=4
tail=0; head=1
tail=4; head=0
"""


class LoopArrayQueue:

    def __init__(self, max_length):
        self.arr = []
        self.max_length = max_length
        for _ in range(max_length):
            self.arr.append(None)

        self.head = 0
        self.tail = 0

    def enqueue(self, item):
        if (self.tail + 1) % self.max_length == self.head:
            return False
        
        self.arr[self.tail] = item
        if self.tail == self.max_length - 1:
            self.tail = 0
        else:
            self.tail += 1

        print(self.arr)

    def dequeue(self):
        if self.head == self.tail:
            return None

        res = self.arr[self.head]

        if self.head == self.max_length - 1:
            self.head = 0
        else:
            self.head += 1

        print(self.arr)
        return res


if __name__ == '__main__':
    q = LoopArrayQueue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.dequeue()
    q.enqueue(5)
    q.dequeue()
    q.enqueue(6)

