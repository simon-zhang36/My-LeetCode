class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = None

    def _getNode(self, index):
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index > self.size - 1:
            return -1

        return self._getNode(index).val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        node.next = self.head
        self.head = node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        tail = self._getNode(self.size -1)
        node = Node(val)
        tail.next = node
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        Note: if index is smaller than 0, then add at head (not mentioned in the question)
        """
        if index > self.size:
            return
        if index < 0 or index == 0:
            self.addAtHead(val)
        else:
            node_before_index = self._getNode(index-1)
            node = Node(val)
            node.next = node_before_index.next
            node_before_index.next = node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index > self.size-1:
            return

        if index == 0:
            self.head = self.head.next
        else:
            node_before_index = self._getNode(index - 1)
            node_before_index.next = node_before_index.next.next

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1, 2)
# obj.get(1)
# obj.deleteAtIndex(1)
# obj.get(1)
#
# obj.addAtIndex(-1, 0)
# obj.get(0)