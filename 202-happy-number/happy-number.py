class Solution:
    def isHappy(self, n: int) -> bool:
        
        num = set()
        while n !=1 and n not in num:
            num.add(n)
            n = sum(int(x)**2 for x in str(n))
        return n == 1