from line.simple_line_sentinel import SimpleLine


class LineQueue:

    def __init__(self, max_length):
        self.line = SimpleLine()
        self.max_length = max_length

    def enqueue(self, item):
        if self.line.length() == self.max_length:
            return False
        
        self.line.append(item)
        print(list(self.line.travel()))

    def dequeue(self):
        if not self.line.length():
            return None
        
        self.line.delete(0)
        print(list(self.line.travel()))


if __name__ == '__main__':
    q = LineQueue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.dequeue()
    q.enqueue(6)
    q.enqueue(7)



