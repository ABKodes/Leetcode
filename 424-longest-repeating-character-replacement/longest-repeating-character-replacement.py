class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxSubstring = 0
        left = 0
        counter = {chr(i): 0 for i in range(ord("A"), ord("Z") + 1)}
        for right in range(len(s)):
            counter[s[right]] += 1
            while (right - left + 1) - max(counter.values()) > k:
                counter[s[left]] -= 1
                left += 1
            maxSubstring = max(maxSubstring, right - left + 1)
        return maxSubstring
