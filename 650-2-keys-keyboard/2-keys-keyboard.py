class Solution:
    def minSteps(self, n: int) -> int:
        total = 0
        for i in range(2,n):
            while n % i == 0:
                total +=i
                n//=i
        if n > 1:
            total += n
        return total