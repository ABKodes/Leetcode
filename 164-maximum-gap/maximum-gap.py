class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return 0
        maxsub = 0
        nums.sort()
        for i in range(1,len(nums)):
            maxsub = max(maxsub,nums[i] - nums[i-1])
        return maxsub