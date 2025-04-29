class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = [[interval[0], index] for index,interval in enumerate(intervals)]
        starts.sort()
        result = []
        for interval in intervals:
            end = interval[1]
            found = False
            for start, index in starts:
                if start >= end:
                    result.append(index)
                    found = True
                    break
            if not found:
                result.append(-1)
        return result