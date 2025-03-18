class Solution:
    def smallestNumber(self, num: int) -> int:
        negative = False
        if num < 0:
            negative = True
        temp = [int(digit) for digit in str(abs(num))]
        if negative:
            temp.sort(reverse=True)
        else:
            temp.sort()
            if 0 in temp:
                for i in range(len(temp)):
                    if temp[i] != 0:
                        temp[0], temp[i] = temp[i], temp[0]
                        break
        temp = [str(digit) for digit in temp]
        result = int("".join(temp))
        return result * -1 if negative else result