class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        maxLength = max(len(word1), len(word2))
        resultList = []
        for i in range(maxLength):
            if i < len(word1):
                resultList.append(word1[i])
            if i < len(word2):
                resultList.append(word2[i])
        return ''.join(resultList)