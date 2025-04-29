class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        currentDir = ""
        # Added / to append the last directory
        for dir in path + "/":
            if dir == "/":
                # Moving up one directory
                if currentDir == "..":
                    if stack:
                        stack.pop()
                # Valid directory
                elif currentDir != "" and currentDir != ".":
                    stack.append(currentDir)
                currentDir = ""
            else:
                currentDir += dir
        return "/" + "/".join(stack)