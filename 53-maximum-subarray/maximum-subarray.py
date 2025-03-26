class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = maxSum = nums[0]
    
        left = 0
        for right in range(1, len(nums)):
            if currentSum < 0:
                left = right
                currentSum = nums[right]
            else:
                currentSum += nums[right]
            maxSum = max(maxSum, currentSum)
        return maxSum