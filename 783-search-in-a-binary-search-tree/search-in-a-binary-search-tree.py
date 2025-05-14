# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(root, target):
            if not root:
                return None
            if target > root.val:
                return search(root.right, target)
            elif target < root.val:
                return search(root.left,target)
            else:
                return root
        return search(root,val)