class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = set("qwertyuiop")
        secondRow = set("asdfghjkl")
        thirdRow = set("zxcvbnm")
        result = []
        for word in words:
            temp = set(word.lower())
            if temp.issubset(firstRow) or temp.issubset(secondRow) or temp.issubset(thirdRow):
                result.append(word)
        return result