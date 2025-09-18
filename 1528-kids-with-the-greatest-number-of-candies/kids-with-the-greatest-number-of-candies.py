class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxNumber = max(candies)
        result = []
        for i in range(len(candies)):
            candies[i] = candies[i] + extraCandies
            result.append(candies[i]>=maxNumber)
        return result
        