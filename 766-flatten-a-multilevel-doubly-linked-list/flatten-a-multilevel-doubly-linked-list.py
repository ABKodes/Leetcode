"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        current = head
        while current:
            if current.child:
                # Saving the next node of original list
                nextNode = current.next

                # Recursively flatten child node
                childHead = self.flatten(current.child)
                current.child = None

                # Connect current node to the head of child list
                current.next = childHead
                childHead.prev = current

                # Traverse to the end of the child list
                while childHead.next:
                    childHead = childHead.next
                
                # Connect it to the nextNode of original list
                childHead.next = nextNode
                if nextNode:
                    nextNode.prev = childHead
                
            current = current.next
        return head