class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def maxPick(left,right):
            if left == right:
                return nums[left]
            pickLeft = nums[left] - maxPick(left+1,right)
            pickRight = nums[right] - maxPick(left,right-1)
            return max(pickLeft,pickRight)
        return maxPick(0,len(nums)-1) >= 0