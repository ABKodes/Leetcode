class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        temp = [int(str(num)[::-1]) for num in nums]
        return len(set(nums + temp))