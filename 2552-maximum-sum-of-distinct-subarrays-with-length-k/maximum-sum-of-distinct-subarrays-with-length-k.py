class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxSum = currentSum = left = 0
        freq = {}
        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            currentSum += nums[right]
            if right - left + 1 > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                currentSum -= nums[left]
                left += 1
            if right - left + 1 == k and len(freq) == k:
                maxSum = max(maxSum, currentSum)    
        return maxSum