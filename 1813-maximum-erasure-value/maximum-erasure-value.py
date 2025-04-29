class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_sum = current_sum = 0
        unique = set()
        left = 0
        for right in range(len(nums)):
            while nums[right] in unique:
                unique.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            unique.add(nums[right])
            current_sum += nums[right]
            max_sum = max(max_sum, current_sum)
        return max_sum
        