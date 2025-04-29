class Solution:
    def clearDigits(self, s: str) -> str:
        digits = set("0123456789")
        stack = []
        for char in s:
            if stack and char in digits:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)