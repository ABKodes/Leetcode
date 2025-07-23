class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        answer = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                answer = max(answer, count)
                count = 0
        answer = max(answer, count)        
        return answer