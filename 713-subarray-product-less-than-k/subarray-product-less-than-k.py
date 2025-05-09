class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        prefix = [1] * (len(nums) + 1)
        for i in range(len(prefix) - 1):
            prefix[i + 1] = prefix[i] * nums[i]
        result = 0

        for j in range(len(nums)):
            left , right = 0, j + 1
            while left < right:
                mid = (left + right)//2
                if prefix[mid] * k > prefix[j + 1]:
                    right = mid
                else:
                    left = mid + 1
            result += (j - left + 1)
        return result
