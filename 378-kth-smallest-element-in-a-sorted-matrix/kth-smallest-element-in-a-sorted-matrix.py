class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                heappush(heap, matrix[row][col])
        return nsmallest(k, heap)[-1]