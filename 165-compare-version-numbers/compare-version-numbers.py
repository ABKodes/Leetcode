class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        temp1 = version1.split(".")
        temp2 = version2.split(".")
        maxLength = max(len(temp1), len(temp2))
        temp1 += [0] * (maxLength - len(temp1))
        temp2 += [0] * (maxLength - len(temp2))
        pointer1 = pointer2 = 0
        while pointer1 < maxLength and pointer2 < maxLength:
            if int(temp1[pointer1]) > int(temp2[pointer2]):
                return 1
            elif int(temp1[pointer1]) < int(temp2[pointer2]):
                return -1
            pointer1 += 1
            pointer2 += 1
        return 0