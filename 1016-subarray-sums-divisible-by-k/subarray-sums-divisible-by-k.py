class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        currentSum = result = 0
        prefixSums = {0:1}
        for num in nums:
            currentSum += num
            remainder = currentSum % k

            result += prefixSums.get(remainder,0)
            prefixSums[remainder] = prefixSums.get(remainder,0) + 1
        
        return result