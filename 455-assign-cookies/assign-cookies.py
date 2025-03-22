class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        left=right=result = 0
        while left < len(g) and right < len(s):
            if g[left] <= s[right]:
                result += 1
                left +=1
            right += 1
        return result