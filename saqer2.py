class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, item):
        if self.count == self.size:
            print("المصفوفة ممتلئة")
            return
        self.buffer[self.rear] = item
        self.rear = (self.rear + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            print("المصفوفة فارغة")
            return None
        item = self.buffer[self.front]
        self.buffer[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return item

    def peek(self):
        if self.count == 0:
            print("المصفوفة فارغة")
            return None
        return self.buffer[self.front]

# مثال على الاستخدام
buffer = CircularBuffer(5)
buffer.enqueue(1)
buffer.enqueue(2)
buffer.enqueue(3)
print(buffer.dequeue())  # 1
print(buffer.peek())      # 2