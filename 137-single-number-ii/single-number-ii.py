class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = Counter(nums)
        for key, value in temp.items():
            if value == 1:
                return key