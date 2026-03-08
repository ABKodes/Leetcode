class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        for i in range(len(s)):
            if i < len(s) - 1 and romanDict[s[i]] < romanDict[s[i + 1]]:
                result -= romanDict[s[i]]
            else:
                result += romanDict[s[i]]
        return result