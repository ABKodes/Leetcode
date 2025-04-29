# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        aheadPointer = dummy
        behindPointer = dummy
        for _ in range(n):
            aheadPointer = aheadPointer.next
        while aheadPointer.next:
            aheadPointer = aheadPointer.next
            behindPointer = behindPointer.next
        behindPointer.next = behindPointer.next.next
        return dummy.next
        
        