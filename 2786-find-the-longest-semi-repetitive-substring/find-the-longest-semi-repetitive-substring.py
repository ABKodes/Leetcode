class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        max_length = 1
        left = repeat_counter = 0
        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                repeat_counter += 1
            
            while repeat_counter > 1:
                if s[left] == s[left + 1]:
                    repeat_counter -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
        
        return max_length
