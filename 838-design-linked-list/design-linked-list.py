class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def addAtHead(self, value: int) -> None:
        newNode = Node(value)  # Use value instead of value
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def addAtTail(self, value: int) -> None:
        newNode = Node(value)  # Use value instead of value
        if not self.head:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        self.size += 1

    def addAtIndex(self, index: int, value: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(value)
            return
        if index == self.size:
            self.addAtTail(value)
            return
        newNode = Node(value)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        newNode.next = current.next
        current.next = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        current = self.head
        if index == 0:
            self.head = current.next
        else:
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

# Example usage:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(value)
# obj.addAtTail(value)
# obj.addAtIndex(index, value)
# obj.deleteAtIndex(index)