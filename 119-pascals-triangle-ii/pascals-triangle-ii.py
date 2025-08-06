class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        @lru_cache(None)
        def pascal(n,k):
            if k == 0 or k == n:
                return 1
            return pascal(n-1,k-1) + pascal(n-1,k)
        return [pascal(rowIndex, k) for k in range(rowIndex + 1)]