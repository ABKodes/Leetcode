class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        checker = Counter(p)
        window = Counter(s[:len(p)-1])
        left,right = 0, len(p) - 1
        result = []
        while right < len(s):
            window[s[right]] +=1
            if window == checker:
                result.append(left)
            window[s[left]] -=1
            if window[s[left]] == 0:
                del window[s[left]]
            left +=1
            right +=1
            print(window)
        return result