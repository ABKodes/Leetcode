# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        result = 0
        def dfs(root):
            if not root:
                return (0,0)
            leftSum,leftCount = dfs(root.left)
            rightSum,rightCount = dfs(root.right)
            totalSum = root.val + leftSum + rightSum
            totalCount = 1 + leftCount + rightCount
            average = totalSum // totalCount
            if root.val == average:
                nonlocal result
                result +=1
            return (totalSum,totalCount)
        dfs(root)
        return result