class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        result = 0
        minDeque = deque()
        maxDeque = deque()

        for right in range(n):
            while minDeque and nums[right] < nums[minDeque[-1]]:
                minDeque.pop()
            minDeque.append(right)
            while maxDeque and nums[right] > nums[maxDeque[-1]]:
                maxDeque.pop()
            maxDeque.append(right)
            # If window is invalid
            while nums[maxDeque[0]] - nums[minDeque[0]] > 2:
                left += 1
                if minDeque[0] < left:
                    minDeque.popleft()
                if maxDeque[0] < left:
                    maxDeque.popleft()
            result += right - left + 1
        return result