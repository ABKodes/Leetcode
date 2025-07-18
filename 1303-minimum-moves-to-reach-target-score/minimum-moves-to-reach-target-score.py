class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:        
        moves = 0
        while target > 1 and maxDoubles > 0:
            if target % 2 == 0:
                target = target // 2
                maxDoubles -= 1
            else:
                target -= 1
            moves += 1
        moves += target - 1
        return moves
        