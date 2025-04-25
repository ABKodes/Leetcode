class DataStream:

    def __init__(self, value: int, k: int):
        self.data = deque(maxlen=k)
        self.maxValue=k
        self.value = value
        self.counter = 0

    def consec(self, num: int) -> bool:
        if len(self.data) == self.maxValue:
            removedValue = self.data.popleft()
            if removedValue == self.value:
                self.counter -= 1
        self.data.append(num)
        if num == self.value:
            self.counter += 1
        return self.counter == self.maxValue


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)