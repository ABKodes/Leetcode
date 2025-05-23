class MyCircularQueue:

    def __init__(self, k: int):
        self.data = []
        self.maxSize = k
    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.data.append(value)
            return True
        return False
    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.data.pop(0)
            return True
        return False
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[0]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[-1]

    def isEmpty(self) -> bool:
        return len(self.data) == 0

    def isFull(self) -> bool:
        return len(self.data) == self.maxSize

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()