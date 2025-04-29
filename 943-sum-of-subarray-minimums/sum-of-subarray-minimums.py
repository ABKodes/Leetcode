class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        total = 0
        stack = []
        arr = [0] + arr + [0]
        for index, value in enumerate(arr):
            while stack and arr[stack[-1]] > value:
                mid = stack.pop()
                left = stack[-1]
                total += arr[mid] * (mid - left) * (index - mid)
                total %= mod
            stack.append(index)
        return total