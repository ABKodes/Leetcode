class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        s = list(s.split(" "))
        if len(s) != len(pattern):
            return False
        totalDict = {}
        for i in range(len(pattern)):
            if pattern[i] in totalDict:
                if totalDict[pattern[i]] != s[i]:
                    return False
            else:
                if s[i] in totalDict.values():
                    return False
            totalDict[pattern[i]] = s[i]
        return True
