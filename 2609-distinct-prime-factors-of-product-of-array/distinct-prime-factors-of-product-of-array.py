class Solution:
    def distinctPrimeFactors(self, nums):
        def prime_factors(n):
            factors = set()
            d = 2
            while d * d <= n:
                while (n % d) == 0:
                    factors.add(d)
                    n //= d
                d += 1
            if n > 1:
                factors.add(n)
            return factors
        
        distinct_primes = set()
        for num in nums:
            distinct_primes.update(prime_factors(num))
        
        return len(distinct_primes)