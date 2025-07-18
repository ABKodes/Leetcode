class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])

        arrows = 1
        previous = points[0][1]
        for i in range(1,len(points)):
            if points[i][0] > previous:
                arrows += 1
                previous = points[i][1]
        
        return arrows