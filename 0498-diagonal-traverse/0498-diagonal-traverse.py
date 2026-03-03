class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        total = n - 1 + m
        l = [[] for _ in range(total)]
        for i in range(n):
            for j in range(m):
                l[i + j].append(mat[i][j])

        sol = []
        for i, subl in enumerate(l):
            if i % 2 == 0:
                sol.extend(subl[::-1])
            else:
                sol.extend(subl)
        
        return sol