class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def dp(idx, cur):
            if idx >= n:
                return int(cur == target)

            return dp(idx + 1, cur + nums[idx]) + dp(idx + 1, cur - nums[idx])
        return dp(0, 0)