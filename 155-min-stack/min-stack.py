class MinStack:

    def __init__(self):
        self.define = []

    def push(self, val: int) -> None:
        self.define.append(val)

    def pop(self) -> None:
        self.define.pop()

    def top(self) -> int:
        return self.define[-1]

    def getMin(self) -> int:
        return min(self.define)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()