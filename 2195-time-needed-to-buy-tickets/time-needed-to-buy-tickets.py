class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # Initialize the queue
        queue = deque()
        for i in range(len(tickets)):
            queue.append(i)
        # Time tracker
        timeNeeded = 0
        # Process the queue
        while len(queue) != 0:
            timeNeeded += 1
            front = queue[0]
            queue.popleft()
            tickets[front] -= 1
            # Check if the target person is done
            if tickets[front] == 0 and k == front:
                return timeNeeded
            # Re-add to queue if still has tickets
            if tickets[front] != 0:
                queue.append(front)
        return timeNeeded