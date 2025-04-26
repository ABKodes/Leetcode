"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        unique = {None:None}
        current = head
        index = 0

        while current:
            newPointer = Node(current.val)
            unique[current] = newPointer
            current = current.next
        
        old = head
        while old:
            unique[old].next = unique[old.next]
            unique[old].random = unique[old.random]
            old = old.next
        
        return unique[head]