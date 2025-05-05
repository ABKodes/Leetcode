class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b, c = 1, 1, 2
        for _ in range(3, n + 1):
            d = (2 * c + a) % MOD
            a, b, c = b, c, d
        return c