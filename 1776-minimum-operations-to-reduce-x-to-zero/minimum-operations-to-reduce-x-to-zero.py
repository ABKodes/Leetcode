class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left = currentSum = 0
        maxLength = -1
        target = sum(nums) - x
        for right in range(len(nums)):
            currentSum += nums[right]
            while currentSum > target and left <= right:
                currentSum -= nums[left]
                left += 1
            if currentSum == target:
                maxLength = max(maxLength, right - left + 1)
        return len(nums) - maxLength if maxLength != -1 else -1