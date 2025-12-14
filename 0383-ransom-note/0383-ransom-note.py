class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomDict = {}
        magDict = {}
        for char in ransomNote:
            ransomDict[char] = ransomDict.get(char,0) + 1
        for char in magazine:
            magDict[char] = magDict.get(char,0) + 1
        for key in ransomDict.keys():
            if key not in magDict:
                return False
            if ransomDict[key] > magDict[key]:
                return False
        return True
        