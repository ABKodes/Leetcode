class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        root = {i: i for i in range(n)}
        rank = [0] * n

        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            
            return root[x]
        
        def union(x, y):
            x, y = find(x), find(y)

            if x == y:
                return
            
            if rank[x] < rank[y]:
                root[x] = y
            elif rank[x] > rank[y]:
                root[y] = x
            else:
                root[y] = x
                rank[x] += 1

        for x, y in pairs:
            union(x, y)
        
        comp = defaultdict(list)

        for i in range(n):
            parent = find(i)
            comp[parent].append(i)

        result = ['a'] * n
        
        for indices in comp.values():
            chars = sorted(s[i] for i in indices)
            
            for idx, ch in zip(sorted(indices), chars):
                result[idx] = ch

        return ''.join(result)
