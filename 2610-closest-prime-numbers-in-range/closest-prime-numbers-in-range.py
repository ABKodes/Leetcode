class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        isPrime = [True] * (right + 1)
        isPrime[0:2] = [False, False]

        for i in range(2, int(right ** 0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, right + 1, i):
                    isPrime[j] = False

        primes = [i for i in range(max(2, left), right + 1) if isPrime[i]]
        result = [-1, -1]
        minDiff = float("inf")
        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < minDiff:
                minDiff = diff
                result = [primes[i], primes[i + 1]]
        return result


        