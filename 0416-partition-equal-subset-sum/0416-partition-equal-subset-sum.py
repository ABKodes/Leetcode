class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        for i in range(len(nums)):
            for pd in list(dp):
                if pd+nums[i] == target:
                    return True
                dp.add(pd+nums[i])
        return target in dp