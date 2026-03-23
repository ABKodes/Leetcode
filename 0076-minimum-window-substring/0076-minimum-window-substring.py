class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        window = defaultdict(int)
        require = len(target)
        have = 0
        resultLength = len(s) + 1
        result = [-1, -1]
        left = 0
        for right in range(len(s)):
            window[s[right]] += 1
            if s[right] in target and window[s[right]] == target[s[right]]:
                have += 1
            while have == require:
                if right - left + 1 < resultLength:
                    resultLength = right - left + 1
                    result = [left,right]
                window[s[left]] -= 1
                if s[left] in target and window[s[left]] < target[s[left]]:
                    have -= 1
                left += 1
        start, end = result
        return s[start:end+1] if resultLength != len(s) + 1 else ""
            