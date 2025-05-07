class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        result = right
        total = 0

        while left <= right:
            mid = (left + right) // 2
            divisor = 0
            for num in nums:
                divisor += math.ceil(num/mid)
            if divisor <= threshold:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result