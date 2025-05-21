# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        rootVal = preorder[0]
        root = TreeNode(rootVal)

        # Split it into left and right preorder
        leftPreorder = [x for x in preorder[1:] if x < rootVal]
        rightPreorder = [x for x in preorder[1:] if x > rootVal]

        root.left = self.bstFromPreorder(leftPreorder)
        root.right = self.bstFromPreorder(rightPreorder)

        return root