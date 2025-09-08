class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        result = []
        for num in nums:
            if num in seen:
                result.append(num)
            seen.add(num)
        return result