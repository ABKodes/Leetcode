class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10**9 + 7        
        if p == 1: return 1
        maxNum = (2 ** p) - 1
        k = (2 ** (p-1)) - 1
        term = pow(maxNum - 1, k, MOD)
        return (maxNum % MOD) * term % MOD