class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        times = []

        for time in timePoints:
            hours, minutes = map(int, time.split(':'))
            times.append(60 * hours + minutes)
        
        times.sort()
        result = float('inf')

        for i in range(1, len(times)):
            result = min(result, times[i] - times[i - 1])

        result = min(result, 1440 + times[0] - times[-1])
        return result
        