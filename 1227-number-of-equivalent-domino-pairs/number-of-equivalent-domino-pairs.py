class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        for domino in dominoes:
            key = tuple(sorted(domino))
            count[key] += 1
        
        pairs = 0
        for value in count.values():
            pairs += value * (value - 1) // 2
        return pairs