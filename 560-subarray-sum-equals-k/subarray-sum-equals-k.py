class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        currentSum = 0
        prefixSums = {0:1}

        for num in nums:
            currentSum += num
            difference = currentSum - k

            result += prefixSums.get(difference, 0)
            prefixSums[currentSum] = prefixSums.get(currentSum, 0) + 1
        
        return result
