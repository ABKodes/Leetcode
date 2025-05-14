# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        level = 0
        while queue:
            levelSize = len(queue)
            previousValue = float('-inf') if level % 2 == 0 else float('inf')
            for _ in range(levelSize):
                current = queue.popleft()
                value = current.val
                # Parity Check
                if level % 2 == 0:
                    # Values must be odd and strictly increasing
                    if value % 2 == 0 or value <= previousValue:
                        return False
                else:
                    # Values must be odd and strictly increasing
                    if value % 2 != 0 or value >= previousValue:
                        return False
                previousValue = value
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            
            level += 1
        
        return True
                