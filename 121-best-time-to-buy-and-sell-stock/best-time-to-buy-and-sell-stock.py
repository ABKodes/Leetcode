class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float(inf)
        for price in prices:
            if price < minPrice:
                minPrice = price
            profit = price - minPrice
            if profit > 0:
                maxProfit = max(profit,maxProfit)
        return maxProfit