class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        def canComplete(k):
            selectedTasks = tasks[:k]
            selectedWorkers = workers[-k:]
            remainingPills = pills

            for i in reversed(range(k)):
                task = selectedTasks[i]
                index = bisect.bisect_left(selectedWorkers, task)

                if index < len(selectedWorkers):
                    selectedWorkers.pop(index)
                else:
                    if remainingPills == 0:
                        return False
                    required = task - strength
                    index = bisect.bisect_left(selectedWorkers, required)
                    if index < len(selectedWorkers):
                        selectedWorkers.pop(index)
                        remainingPills -= 1
                    else:
                        return False
            return True
        
        left = 0
        right = min(len(tasks), len(workers))
        answer = 0

        while left <= right:
            mid = (left + right) // 2
            if canComplete(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return answer