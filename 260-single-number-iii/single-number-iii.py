class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        temp = Counter(nums)
        result = []
        for key, value in temp.items():
            if value == 1:
                result.append(key)
        return result