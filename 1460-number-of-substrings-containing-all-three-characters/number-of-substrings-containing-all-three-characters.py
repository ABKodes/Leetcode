class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {"a": 0, "b":0, "c":0}
        result = 0
        left = 0
        for right in range(len(s)):
            count[s[right]] += 1
            # Confirming there's at least one occurrence in the substring
            while count["a"] > 0 and count["b"] > 0 and count["c"] > 0:
                result += len(s) - right 
                count[s[left]] -= 1
                left += 1
        return result 