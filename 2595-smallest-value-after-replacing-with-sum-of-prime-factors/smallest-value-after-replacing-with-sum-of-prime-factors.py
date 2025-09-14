class Solution:
    def smallestValue(self, n: int) -> int:
        def sumPrimeFact(n):
            i = 2
            total = 0
            while i * i <= n:
                while n % i == 0:
                    total += i
                    n //= i
                i += 1
            if n > 1:
                total += n
            return total
        while True:
            sum = sumPrimeFact(n)
            if sum == n:
                return n
            n = sum