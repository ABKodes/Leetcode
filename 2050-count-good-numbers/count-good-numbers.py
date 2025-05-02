class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        def mod_pow(base, exponent):
            if exponent == 0:
                return 1
            half = mod_pow(base, exponent // 2)
            half = (half * half) % MOD
            if exponent % 2 == 0:
                return half
            else:
                return (half * base) % MOD

        even = (n + 1) // 2
        odd = n // 2
        return (mod_pow(5, even) * mod_pow(4, odd)) % MOD
