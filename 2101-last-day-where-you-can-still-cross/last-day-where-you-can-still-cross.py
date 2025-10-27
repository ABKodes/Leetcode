class Solution: #using dfs
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        def can_cross(d):
            g = [[0]*col for _ in range(row)]
            for i in range(d):
                r,c = cells[i]
                g[r-1][c-1] = 1
            q = deque()
            for j in range(col):
                if g[0][j]==0:
                    q.append((0,j)); g[0][j]=1
            while q:
                x,y=q.popleft()
                if x==row-1: return True
                for dx,dy in dirs:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<row and 0<=ny<col and g[nx][ny]==0:
                        g[nx][ny]=1; q.append((nx,ny))
            return False
        lo,hi,ans=1,len(cells),0
        while lo<=hi:
            mid=(lo+hi)//2
            if can_cross(mid): ans=mid; lo=mid+1
            else: hi=mid-1
        return ans
