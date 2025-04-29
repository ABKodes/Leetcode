class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        checker = set(nums)
        maxStreak = -1
        for num in nums:
            currentStreak = 1
            currentNum = num
            while currentNum * currentNum in checker:
                currentStreak += 1
                currentNum = currentNum * currentNum
            if currentStreak >= 2:
                maxStreak = max(maxStreak, currentStreak)
        return maxStreak
