class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        count = []
        for i in range(len(s)):
            if stack and stack[-1] == s[i]:
                count[-1]+=1
            else:
                stack.append(s[i])
                count.append(1)
            if count[-1]==k:
                count.pop()
                stack.pop()
        ans = ""
        for i in range(len(stack)):
            ans += stack[i]*count[i]
        return ans