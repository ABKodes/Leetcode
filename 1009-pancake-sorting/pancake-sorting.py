class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        length = len(arr)
        for i in range(length):
            # Finding the max value and it's index
            maxValue = max(arr[:length-i])
            maxValueIndex = arr.index(maxValue) + 1
            # Reversing the max value to put it into the first position
            arr[:maxValueIndex] = reversed(arr[:maxValueIndex])
            result.append(maxValueIndex)
            # Reversing the max value again to put it into the designated position
            arr[:length - i] = reversed(arr[:length - i])
            result.append(length - i)
        return result