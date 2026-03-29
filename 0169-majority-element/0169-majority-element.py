class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freq = Counter(nums)
        for key,value in freq.items():
            if value > n / 2:
                return key