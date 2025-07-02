class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        freq_dict = {0:1}
        cum_sum = 0
        count = 0

        for num in nums:
            cum_sum += num % 2
            count += freq_dict.get(cum_sum - k, 0)
            freq_dict[cum_sum] = freq_dict.get(cum_sum, 0) + 1
        
        return count