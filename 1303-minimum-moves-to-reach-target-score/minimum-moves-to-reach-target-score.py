class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        # Can you run it and check 
        
        #  I'm just testing sth
        # Did you understand the question
        # def power(n):
        #     return n > 0 and math.log2(n).is_integer()
        # moves = 0
        # while target > 1 and maxDoubles > 0:
        #     if maxDoubles > 0 and power(target):
        #         target = target // 2
        #         moves += 1
        #         maxDoubles -= 1
        #     elif maxDoubles > 0 and not power(target):
        #         target = target - 1
        #         moves += 1
        #     elif maxDoubles == 0:
        #         moves += target - 1
        #         break
        # print(moves)
        # why are we getting time limit exceeded 
        # I don't know i'm just checking it 
        # I didn't name the function right that's why let me check i
        
        
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
        