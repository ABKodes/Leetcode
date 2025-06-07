class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, columns = len(board), len(board[0])
        path = set()

        def dfs(row, column, i):
            if i == len(word):
                return True
            if (row < 0 or column < 0 or row >= rows or column >= columns or word[i] != board[row][column] or (row,column) in path):
                return False
            path.add((row, column))
            result = (dfs(row + 1, column, i + 1) or dfs(row - 1, column, i + 1) or dfs(row, column + 1, i + 1) or dfs(row, column - 1, i + 1))

            path.remove((row, column))
            return result
        
        for r in range(rows):
            for c in range(columns):
                if dfs(r,c,0):
                    return True
        return False