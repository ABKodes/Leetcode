class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squareRoot = int(math.sqrt(c))
        arr = [i * i for i in range(squareRoot + 1)]
        left , right = 0, len(arr) - 1
        while left <= right:
            if arr[left] + arr[right] == c:
                return True
            elif arr[left] + arr[right] < c:
                left += 1
            else:
                right -= 1
        return False