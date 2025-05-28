class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        checker = {2,3,5}
        for factor in checker:
            while n % factor == 0:
                n //= factor
        return n == 1