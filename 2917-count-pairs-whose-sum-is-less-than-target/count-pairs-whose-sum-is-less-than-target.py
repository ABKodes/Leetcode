class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        counter = 0
        left,right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                counter += (right - left)
                left += 1
            else:
                right -= 1
        return counter