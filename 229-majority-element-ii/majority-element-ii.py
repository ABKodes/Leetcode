class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        n = len(nums)
        res = []
        for key,value in freq.items():
            if value > math.floor(n/3):
                res.append(key)
        return res