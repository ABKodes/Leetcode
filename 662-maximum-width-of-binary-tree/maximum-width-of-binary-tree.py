# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 0)])
        maxWidth = 0
        while queue:
            levelSize = len(queue)
            _,firstIndex = queue[0]
            for _ in range(levelSize):
                node, index = queue.popleft()
                if node.left:
                    queue.append((node.left, index * 2))
                if node.right:
                    queue.append((node.right, index * 2 + 1))
            # _, lastIndex = queue[-1] if queue else (None, index)
            maxWidth = max(maxWidth, index - firstIndex + 1)
        return maxWidth