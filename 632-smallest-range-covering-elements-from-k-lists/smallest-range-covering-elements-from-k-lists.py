class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        mergedList = []
        for listIndex, numbers in enumerate(nums):
            for number in numbers:
                mergedList.append([number,listIndex])
        
        mergedList.sort()
        # Sliding window

        left = 0
        freq = {}
        result = [-inf,inf]
        required = len(nums)

        for right in range(len(mergedList)):
            currentNum, currentIndex = mergedList[right]
            freq[currentIndex] = freq.get(currentIndex,0) + 1
        
            while len(freq) == required:
                currentRangeStart = mergedList[left][0]
                currentRangeEnd = mergedList[right][0]
                currentRange = currentRangeEnd - currentRangeStart

                if currentRange < (result[1] - result[0]):
                    result = [currentRangeStart, currentRangeEnd]

                leftNum, leftIndex = mergedList[left]
                freq[leftIndex] -= 1
                if freq[leftIndex] == 0:
                    del freq[leftIndex]
                left += 1
        return result

