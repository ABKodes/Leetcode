class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lookUp = {}
        for i in range(len(s)):
            lookUp[s[i]] = i
        stack = []
        seen = set()
        for i in range(len(s)):
            if s[i] in seen:
                continue
            while stack and stack[-1] > s[i] and lookUp[stack[-1]] > i:
                seen.remove(stack[-1])
                stack.pop()
            seen.add(s[i])
            stack.append(s[i])
        return "".join(stack)