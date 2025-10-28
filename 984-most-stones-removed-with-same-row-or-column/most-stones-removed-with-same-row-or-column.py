class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = list(range(n))
        rank = [0] * n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
        for i in range(n):
            for j in range(i+1 , n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i, j)
        components = len(set(find(i) for i in range(n)))
        return n - components

        