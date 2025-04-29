class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            while stack and (stack[-1] > 0 and asteroids[i] < 0):
                if abs(stack[-1]) == abs(asteroids[i]):
                    stack.pop()
                    asteroids[i] = 0
                    break
                elif abs(stack[-1]) < abs(asteroids[i]):
                    stack.pop()
                else:
                    asteroids[i] = 0
            if asteroids[i] != 0:
                stack.append(asteroids[i])
        return stack
                