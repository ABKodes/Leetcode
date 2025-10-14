class Solution:
    @cache
    def backtrack(self, i, j, target):
        if self.done:
            return 0
        if j - i < 1:
            self.done = True
            return 0
            
        res = 0
        
        if self.nums[i] + self.nums[i + 1] == target:
            res = max(res, self.backtrack(i + 2, j, target) + 1)
        if self.nums[j] + self.nums[j - 1] == target:
            res = max(res, self.backtrack(i, j - 2, target) + 1)
        if self.nums[i] + self.nums[j] == target:
            res = max(res, self.backtrack(i + 1, j - 1, target) + 1)
            
        return res
        
    def maxOperations(self, nums: List[int]) -> int:
        self.nums = nums
        self.done = False
        res = 0
        
        res = max(res, self.backtrack(2, len(nums) - 1, nums[0] + self.nums[1]) + 1)
        res = max(res, self.backtrack(0, len(nums) - 3, nums[-1] + nums[-2]) + 1)
        res = max(res, self.backtrack(1, len(nums) - 2, nums[0] + nums[-1]) + 1)
        
        return res