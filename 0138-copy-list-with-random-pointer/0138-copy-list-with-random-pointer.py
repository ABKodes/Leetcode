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
        # If the input list is empty, return None as there's nothing to copy
        if not head:
            return None

        # Step 1: Create a dictionary to map original nodes to their copies
        nodeMap = {}

        # Step 2: Create a copy of each node (excluding the `next` and `random` pointers for now)
        current = head
        while current:
            newNode = Node(current.val)  # Create a new node with the same value
            nodeMap[current] = newNode  # Map the original node to the new node
            current = current.next      # Move to the next node in the original list

        # Step 3: Assign the `next` and `random` pointers for the copied nodes
        current = head
        while current:
            # If the original node has a `next`, set the corresponding `next` pointer in the copy
            if current.next:
                nodeMap[current].next = nodeMap[current.next]

            # If the original node has a `random`, set the corresponding `random` pointer in the copy
            if current.random:
                nodeMap[current].random = nodeMap[current.random]

            # Move to the next node in the original list
            current = current.next

        # Step 4: Return the head of the copied linked list
        return nodeMap[head]
