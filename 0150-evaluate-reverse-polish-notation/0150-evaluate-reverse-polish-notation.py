class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = set('+-*/')
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in op:
                b = stack.pop()
                a = stack.pop()
                if tokens[i] == "+":
                    stack.append(a + b)
                elif tokens[i] == "-":
                    stack.append(a - b)
                elif tokens[i] == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(tokens[i]))
        return stack[0]