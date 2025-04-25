class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        result, depth = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1
                if s[i-1] == '(':
                    result += 2 ** depth
        return result