class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minOperations = float("inf")
        left = 0
        whiteCount = 0
        for right in range(len(blocks)):
            if blocks[right] == "W":
                whiteCount += 1
            
            if right - left + 1 == k:
                minOperations = min(minOperations, whiteCount)
                if blocks[left] == "W":
                    whiteCount -= 1
                left += 1
                
        return minOperations