class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left, right = 1, position[-1] - position[0]
        result = 0
        
        def canPlace(minForce):
            lastPosition = position[0]
            ballsPlaced = 1
            for i in range(1, len(position)):
                if position[i] - lastPosition >= minForce:
                    lastPosition = position[i]
                    ballsPlaced += 1
                    if ballsPlaced == m:
                        return True
            return ballsPlaced >= m

        while left <= right:
            mid = (left + right) // 2
            if canPlace(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result
