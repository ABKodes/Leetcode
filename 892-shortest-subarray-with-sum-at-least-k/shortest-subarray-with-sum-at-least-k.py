class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        queue = deque([(-1, 0)])
        currentSum = 0
        index = 0
        shortLength = float('inf')
        for num in nums:
            currentSum += num
            while queue and currentSum - queue[0][1] >= k:
                shortLength = min(shortLength, index - queue.popleft()[0])
            while queue and currentSum <= queue[-1][1]:
                queue.pop()
            queue.append((index,currentSum))
            index +=1
        return -1 if shortLength == float('inf') else shortLength
                