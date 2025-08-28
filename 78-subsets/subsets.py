class Solution:
    def subsets(self, nums):
        def backtrack(first=0, curr=[]):
            output.append(curr[:])
            for i in range(first, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        
        output = []
        backtrack()
        return output

# Example Usage
# sol = Solution()
# print(sol.subsets([1, 2, 3]))