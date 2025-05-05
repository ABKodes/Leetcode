class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.extend([float('-inf'), float('inf')])
        heaters.sort()
        radius = 0
        i = 1
        for house in houses:
            while heaters[i] < house:
                i += 1
            minDistance = min(house - heaters[i - 1], heaters[i] - house)
            radius = max(radius, minDistance)
        return radius