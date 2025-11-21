class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        diff = [0] * (n+1)

        for start, end, direction in shifts:
            if direction == 1:
                diff[start] += 1
                diff[end+1] -= 1
            else:
                diff [start] -= 1
                diff[end+1] += 1

        # abc
        # 0, 1, 1, -2
        result = []
        shift_amount = 0

        # compute the prefix
        for i in range(1, n+1):
            diff[i] += diff[i-1]
        # 0, 1, 2, 0
        for i in range(n):
            new_char = chr(((ord(s[i]) - ord('a') + diff[i]) % 26) + ord('a'))
            result.append(new_char)

        return "".join(result)


