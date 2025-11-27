class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31 - 1 or x < (-2) ** 31:
            return 0
        result = str(abs(x))
        result = result[::-1]
        if int(result) >= 2**31 - 1 or int(result) < (-2) ** 31:
            return 0
        else:
            if x < 0:
                x = -1 * int(result)
            else:
                x = int(result)
        return x