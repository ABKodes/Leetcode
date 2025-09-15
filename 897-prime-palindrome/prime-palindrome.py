class Solution:
    def primePalindrome(self, n: int) -> int:
        for p in (2, 3, 5, 7, 11):
            if n <= p: return p
        if len(str(n)) % 2 == 0:
            n = 10 ** len(str(n))

        def is_prime(x: int) -> bool:
            if x % 2 == 0 or x % 3 == 0: return False
            f = 5
            while f * f <= x:
                if x % f == 0 or x % (f + 2) == 0: return False
                f += 6
            return True

        i = max(1, int(str(n)[: (len(str(n)) + 1) // 2]))
        while True:
            s = str(i)
            x = int(s + s[-2::-1])  # odd-length palindrome
            if x >= n and is_prime(x): return x
            i += 1