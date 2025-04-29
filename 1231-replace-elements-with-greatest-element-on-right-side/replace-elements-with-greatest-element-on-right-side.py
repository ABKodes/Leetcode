class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxValue = -1
        for i in range(len(arr) - 1, -1 , -1):
            current = arr[i]
            arr[i] = maxValue
            maxValue = max(maxValue, current)
        return arr