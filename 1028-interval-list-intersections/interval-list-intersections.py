class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        left=right=0
        result = []
        while left < len(firstList) and right < len(secondList):
            firstValue = max(firstList[left][0], secondList[right][0])
            secondValue = min(firstList[left][1], secondList[right][1])
            if firstValue <= secondValue:
                result.append([firstValue, secondValue])
                if firstList[left][1] < secondList[right][1]:
                    left +=1
                else:
                    right +=1
            else:
                if firstList[left][1] < secondList[right][1]:
                    left +=1
                else:
                    right +=1
        return result