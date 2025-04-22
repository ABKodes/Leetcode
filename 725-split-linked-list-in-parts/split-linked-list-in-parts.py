# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        result = []
        total = 0
        current = head 
        while current:
            total +=1
            current = current.next
        
        # Declaring the part and extra
        part = total // k
        extra = total % k

        current = head
        for _ in range(k):
            partHead = current
            currentPartSize = part
            if extra:
                currentPartSize +=1
                extra -= 1

            for _ in range(currentPartSize -1):
                if current:
                    current = current.next
            if current:
                nextPart = current.next
                current.next = None
                current = nextPart
            
            result.append(partHead)
        return result