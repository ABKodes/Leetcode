class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse = True)
        processorTime.sort()
        maxTime = 0
        for i in range(len(processorTime)):
            taskBatch = tasks[4 * i: (i + 1) * 4]
            currentMax = processorTime[i] + taskBatch[0]
            maxTime = max(currentMax, maxTime)
        return maxTime
