class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        first = 1
        second = 2
        for _ in range(3,n+1):
            current = first + second
            first = second
            second = current
        return second