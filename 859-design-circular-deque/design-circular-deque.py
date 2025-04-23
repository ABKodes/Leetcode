class MyCircularDeque:

    def __init__(self, k: int):
        self.max_size = k
        self.data = []
    def insertFront(self, value: int) -> bool:
        if len(self.data) >= self.max_size:
            return False
        else:
            self.data.insert(0,value)
            return True
    def insertLast(self, value: int) -> bool:
        if len(self.data) >= self.max_size:
            return False
        else:
            self.data.append(value)
            return True
    def deleteFront(self) -> bool:
        if len(self.data) > 0:
            self.data = self.data[1:]
            return True
        return False
    def deleteLast(self) -> bool:
        if len(self.data) > 0:
            self.data = self.data[:-1]
            return True
        return False
    def getFront(self) -> int:
        if len(self.data) > 0:
            return self.data[0]
        return -1
    def getRear(self) -> int:
        if len(self.data) > 0:
            return self.data[-1]
        return -1
    def isEmpty(self) -> bool:
        return len(self.data) == 0
    def isFull(self) -> bool:
        return len(self.data) == self.max_size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()