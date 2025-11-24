class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = []
        total = sum([n for n in nums if n % 2 == 0])

        for val, i in queries:
            if nums[i] % 2 == 0:
                total -= nums[i]

            nums[i] += val

            if nums[i] % 2 == 0:
                total += nums[i]

            result.append(total) 

        return result
        
