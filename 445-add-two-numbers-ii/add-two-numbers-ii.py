# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(current):
            prev = None
            while current:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            return prev
        newL1 = reverse(l1)
        newL2 = reverse(l2)
        dummy = ListNode(-1)
        current = dummy
        carry = 0

        while newL1 or newL2 or carry:
            value1 = newL1.val if newL1 else 0
            value2 = newL2.val if newL2 else 0
            value = value1 + value2 + carry
            carry = value // 10
            value %= 10
            current.next = ListNode(value)
            current = current.next
            newL1 = newL1.next if newL1 else None
            newL2 = newL2.next if newL2 else None
        return reverse(dummy.next)
