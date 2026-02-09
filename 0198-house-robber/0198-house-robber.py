class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        x = max(nums[0], nums[1])
        y = nums[0]
        for i in range(2, len(nums)):
            cur = max(x, y + nums[i])
            y = x
            x = cur
        return x