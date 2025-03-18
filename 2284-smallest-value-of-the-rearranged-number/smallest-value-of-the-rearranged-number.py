class Solution:
    def smallestNumber(self, num: int) -> int:
        negative = num < 0
        digits = list(str(abs(num)))
        if negative:
            digits.sort(reverse=True)
        else:
            digits.sort()
            if digits[0] == "0":
                for i in range(1, len(digits)):
                    if digits[i] != "0":
                        digits[0], digits[i] = digits[i], digits[0]
                        break
        result = int("".join(digits))
        return -result if negative else result