class Solution:
    def firstUniqChar(self, s: str) -> int:
        charDict = {}
        for char in s:
            charDict[char] = charDict.get(char,0) + 1
        for index, char in enumerate(s):
            if charDict[char] == 1:
                return index
        return -1