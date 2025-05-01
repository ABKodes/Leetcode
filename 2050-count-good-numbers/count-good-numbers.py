class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        def helper(base,exponent):
            result = 1
            while exponent > 0:
                if exponent % 2 == 1:
                    result = (result * base) % MOD
                base = (base * base) % MOD
                exponent //= 2
            return result
        even = (n+1)//2
        odd = n//2
        return (helper(5,even) * helper(4,odd)) % MOD