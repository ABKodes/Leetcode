# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node, maxValue):
            if not node:
                return None, maxValue
            newNext, newMax = helper(node.next, maxValue)
            if node.val < newMax:
                return newNext, newMax
            else:
                node.next = newNext
                return node, max(node.val, newMax)
            
        newHead, _ = helper(head, float('-inf'))
        return newHead
        

            