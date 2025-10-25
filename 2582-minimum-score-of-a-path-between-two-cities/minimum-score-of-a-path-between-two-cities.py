class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        x = defaultdict(list)
        for i, j, k in roads:
            x[i].append((j, k))
            x[j].append((i, k))

        res = [float("inf")]
        visit = set()

        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            for j, k in x[i]:
                res[0] = min(res[0], k)
                dfs(j)

        dfs(1)
        return res[0]