class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        myTime = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            x, y = ghost
            ghostTime = abs(target[0] - x) + abs(target[1] - y)
            if ghostTime <= myTime:
                return False
        return True