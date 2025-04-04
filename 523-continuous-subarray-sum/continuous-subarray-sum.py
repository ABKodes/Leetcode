class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainderDict = {0: -1}
        total = 0

        for index, number in enumerate(nums):
            total += number
            remainder = total % k
            if remainder not in remainderDict:
                remainderDict[remainder] = index
            elif index - remainderDict[remainder] > 1:
                return True
        return False 