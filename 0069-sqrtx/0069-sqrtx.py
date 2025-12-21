class Solution:
    def mySqrt(self, x: int) -> int:
        value = 0
        while value * value <=x:
            value +=1
        return value -1