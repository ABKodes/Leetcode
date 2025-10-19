class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        segments = []
        cur = ""
    
        for c in s:
            cur += c
            if cur not in seen:
                segments.append(cur)
                seen.add(cur)
                cur = ""
        
        return segments
