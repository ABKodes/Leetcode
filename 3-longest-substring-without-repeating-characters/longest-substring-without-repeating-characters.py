class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        maxLength = 0
        for right in range(len(s)):
            char = s[right]
            while char in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        return maxLength