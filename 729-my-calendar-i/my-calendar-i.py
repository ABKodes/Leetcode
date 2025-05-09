class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        index = bisect.bisect_right(self.events, (startTime, endTime))
        
        if index > 0 and self.events[index - 1][1] > startTime:
            return False
        
        if index < len(self.events) and self.events[index][0] < endTime:
            return False

        self.events.insert(index, (startTime, endTime))
        return True
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)