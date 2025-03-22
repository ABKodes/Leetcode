class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        increasing = decreasing = 1
        maxLength = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                increasing = decreasing + 1
                decreasing = 1
            elif arr[i] < arr[i - 1]:
                decreasing = increasing + 1
                increasing = 1
            else:
                increasing = decreasing = 1

            maxLength = max(maxLength, increasing, decreasing)
        return maxLength
                