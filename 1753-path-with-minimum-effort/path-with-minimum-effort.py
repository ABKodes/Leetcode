class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        r = len(heights) 
        c = len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ef = [[float('inf')] * c for _ in range(r)]
        ef[0][0] = 0

        heap = [(0, 0, 0)]

        while heap:
            effort, row, col = heapq.heappop(heap)

            if row == r - 1 and col == c - 1:
                return effort
            
            for di, dj in directions:
                new_r, new_c = di + row, dj + col
                if 0 <= new_r < r and 0 <= new_c < c:
                    new_effort = max(effort, abs(heights[new_r][new_c] - heights[row][col]))
                    if new_effort < ef[new_r][new_c]:
                        ef[new_r][new_c] = new_effort
                        heapq.heappush(heap, (new_effort, new_r, new_c))