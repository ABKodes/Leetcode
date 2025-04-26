class RecentCounter:

    def __init__(self):
        self.data = deque()

    def ping(self, t: int) -> int:
        self.data.append(t)
        while self.data[0] < t - 3000:
            self.data.popleft()
        return len(self.data)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)