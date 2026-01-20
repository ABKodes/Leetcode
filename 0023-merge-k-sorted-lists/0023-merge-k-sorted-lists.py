# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp = []
        for sub in lists:
            current = sub
            while current:
                temp.append(current.val)
                current = current.next
        temp.sort()
        if not temp:
            return None
        head = ListNode(temp[0])
        current = head
        for value in temp[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

