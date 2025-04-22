class Solution:
    def firstUniqChar(self, s: str) -> int:
        charDict = {}
        for char in s:
            charDict[char] = charDict.get(char,0) + 1
        for key,value in charDict.items():
            if value == 1:
                for i in range(len(s)):
                    if s[i] == key:
                        return i
        return -1