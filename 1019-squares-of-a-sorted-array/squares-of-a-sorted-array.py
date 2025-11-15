class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1

        result = []

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                result.append(nums[l]**2)
                l+=1
            else:
                result.append(nums[r]**2)
                r-=1
        return result[::-1]


        