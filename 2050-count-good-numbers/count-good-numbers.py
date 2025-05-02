class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        # Calculate base ** exponent
        def helper(base, exponent):
            # Base Case
            if exponent == 0:
                return 1
            half = helper(base, exponent // 2)
            result = (half * half) % MOD
            if exponent % 2 == 0:
                return result
            else:
                return (result * base) % MOD
        
        even = (n + 1) // 2
        odd = n // 2

        return (helper(5, even) * helper(4, odd)) % MOD

       
