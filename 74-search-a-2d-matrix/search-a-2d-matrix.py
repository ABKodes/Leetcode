class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for num in matrix:
            if target >= min(num) and target <= max(num):
                left,right = 0,len(num) - 1
                while left <= right:
                    mid = (left+right)//2
                    if num[mid] == target:
                        return True
                    elif num[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
        return False