class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        replacements = 0
        currentMax = nums[-1]

        for i in range(n-2, -1, -1):
            if nums[i] > currentMax:
                parts = (nums[i] + currentMax - 1) // currentMax
                replacements += parts - 1
                currentMax = nums[i] // parts
            else:
                currentMax = nums[i]
        return replacements