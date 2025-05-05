# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            middle = (left + right) // 2
            if isBadVersion(middle) == False:
                left = middle + 1
            else:
                result = middle
                right = middle - 1
        return result