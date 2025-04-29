class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        maxLength = 1
        left = 0
        currentMask = 0

        for right in range(0,len(nums)):
            while (currentMask & nums[right]) != 0:
                currentMask = currentMask ^ nums[left]
                left += 1
            currentMask = currentMask | nums[right]
            maxLength = max(maxLength, right - left + 1)
        return maxLength