class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: 
            return False
        maxIndex = arr.index(max(arr))
        if maxIndex == len(arr) - 1 or maxIndex == 0:
            return False
        for i in range(maxIndex - 1):
            if arr[i] >= arr[i + 1]:
                return False
        for i in range(maxIndex, len(arr) - 1):
            if arr[i] <= arr[i + 1]:
                return False
        return True