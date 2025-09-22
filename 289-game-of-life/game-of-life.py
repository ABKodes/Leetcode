class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
        n = len(board)
        m = len(board[0])
        change = []
        for i in range(n):
            for j in range(m):
                live = 0
                for row, col in neighbors:
                    r = i + row
                    c = j + col
                    if r >= 0 and r < n and c >= 0 and c < m and board[r][c] == 1:
                        live += 1
                        
                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        change.append([i, j])
                else:
                    if live == 3:
                        change.append([i, j])
    
        for row, col in change:
            board[row][col] = 1 - board[row][col]