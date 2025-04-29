class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        i = j = 0
        result = 0
        while i < len(houses):
            while j < len(heaters) - 1 and abs(houses[i] - heaters[j]) >= abs(
                houses[i] - heaters[j + 1]
            ):
                j += 1
            distance = abs(houses[i] - heaters[j])
            result = max(distance, result)
            i += 1
        return result
