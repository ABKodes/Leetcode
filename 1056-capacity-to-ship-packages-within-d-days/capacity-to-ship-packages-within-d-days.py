class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isPossible(capacity):
            currentWeight = 0
            daysNeeded = 1
            for weight in weights:
                if currentWeight + weight > capacity:
                    daysNeeded += 1
                    currentWeight = 0
                currentWeight += weight
            return daysNeeded <= days
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right)// 2
            if isPossible(mid):
                right = mid
            else:
                left = mid + 1
        return left 