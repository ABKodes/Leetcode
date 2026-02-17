class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right= 0
        currentSum = 0
        minLength = float("inf")
        while right < len(nums):
            currentSum += nums[right]
            while currentSum >= target:
                minLength = min(minLength,right - left + 1)
                currentSum -= nums[left]
                left +=1
            right +=1
        return 0 if minLength == float("inf") else minLength
            