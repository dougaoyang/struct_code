class ArrayQueue:

    def __init__(self, max_length):
        self.arr = []
        self.max_length = max_length
        for _ in range(max_length):
            self.arr.append(None)

        self.head = 0
        self.tail = 0

    def enqueue_old(self, item):
        """"该方法会让数组即使有空间也无法加入元素"""
        if self.tail == self.max_length:
            return False

        self.arr.append(item)
        self.tail += 1
        print(self.arr[self.head: self.tail])

    def enqueue(self, item):
        if self.tail == self.max_length:
            if self.head == 0:
                # 队列已经没有空间
                return False
            
            # 数组空间满了之后迁移数据
            for idx in range(self.head, self.tail):
                self.arr[idx-self.head] = self.arr[idx]

            self.tail -= self.head
            self.head = 0

        self.arr[self.tail] = item
        self.tail += 1

        print(self.arr[self.head: self.tail])

    def dequeue(self):
        if self.head == self.tail:
            return None

        res = self.arr[self.head]
        self.head += 1
        print(self.arr[self.head: self.tail])
        return res


if __name__ == '__main__':  
    q = ArrayQueue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.dequeue()
    q.enqueue(6)

    # print(q.arr)
