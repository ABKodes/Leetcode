class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10**9 + 7
        def power(base, exponent):
            result = 1
            base = base % MOD
            while exponent > 0:
                if exponent % 2 == 1:
                    result = (result * base) % MOD
                base = (base * base) % MOD
                exponent = exponent // 2
            return result
        
        if p == 1: return 1
        maxNum = (2 ** p) - 1
        k = (2 ** (p-1)) - 1
        term = power(maxNum - 1, k)
        return (maxNum % MOD) * term % MOD