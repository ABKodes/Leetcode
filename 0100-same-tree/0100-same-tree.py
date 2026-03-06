# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(root):
            if not root:
                return None
            queue = deque([root])
            result = []
            while queue:
                current = queue.popleft()
                if current:
                    result.append(current.val)
                    queue.append(current.left)
                    queue.append(current.right)
                else:
                    result.append(None)
            return result
        return bfs(p) == bfs(q)