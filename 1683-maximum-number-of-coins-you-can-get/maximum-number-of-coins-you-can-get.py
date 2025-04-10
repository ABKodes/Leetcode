class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        result = 0
        i = 0
        while i < n:
            if i < n//3:
                i += 1
            else:
                result += piles[i]
                i += 2
        return result