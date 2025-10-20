class Solution:
    def isValid(self, s: str) -> bool:
        valid = {"(": ")", "{": "}", "[":"]"}
        stack = []
        for char in s:
            if char in valid:
                stack.append(char)
            else:
                if stack and valid[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0