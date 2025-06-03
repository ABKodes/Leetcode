class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(open, closed):
            # Valid if open == closed == n
            if open == closed == n:
                result.append("".join(stack))
                return
            # Only add open parentheses if open < n
            if open < n:
                stack.append("(")
                backtrack(open + 1, closed)
                stack.pop()
            # Only add closed parentheses if closed < open
            if closed < open:
                stack.append(")")
                backtrack(open, closed + 1)
                stack.pop()
            
        backtrack(0,0)
        return result