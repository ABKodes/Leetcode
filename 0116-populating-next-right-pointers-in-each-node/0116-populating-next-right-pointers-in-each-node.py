"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return None
        queue = deque([root])
        while queue:
            levelSize = len(queue)
            previousNode = None
            for _ in range(levelSize):
                node = queue.popleft()
                if previousNode:
                    previousNode.next = node
                previousNode = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if previousNode:
                previousNode.next = None
        return root
