class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(target):
            top = 0
            bottom = 0
            for i in range(len(tops)):
                if tops[i] != target and bottoms[i] != target:
                    return -1
                if tops[i] != target:
                    top += 1
                if bottoms[i] != target:
                    bottom += 1
            return min(top, bottom)
        result = check(tops[0])
        if result != -1:
            return result
        return check(bottoms[0])