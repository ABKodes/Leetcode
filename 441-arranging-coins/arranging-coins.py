class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            total = (mid * (mid + 1)) // 2
            if total > n:
                right = mid - 1
            else:
                left = mid + 1
        return right