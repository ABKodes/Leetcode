class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        result = left = pairs = 0
        count = Counter()
        for right in range(len(nums)):
            pairs += count[nums[right]]
            count[nums[right]] += 1

            while pairs >=k:
                count[nums[left]] -= 1
                pairs -= count[nums[left]]
                left += 1
            
            result += left
        return result