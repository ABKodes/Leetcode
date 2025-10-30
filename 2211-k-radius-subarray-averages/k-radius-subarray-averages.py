class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 0:
            return nums
        if 2 * k + 1 > n:
            return [-1] * n
        
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        averages = [-1] * n
        window_size = 2 * k + 1
        for center in range(k, n - k):
            total = prefix_sum[center + k + 1] - prefix_sum[center - k]
            averages[center] = total // window_size
        return averages
