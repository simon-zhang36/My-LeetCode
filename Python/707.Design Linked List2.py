class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.dummy_head = Node()
        self.dummy_tail = Node(None, self.dummy_head, None)
        self.dummy_head.next = self.dummy_tail

    def getNode(self, index: int) -> int:
        """
        Get the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            raise IndexError

        # search from the head
        if index <= self.size / 2:
            node = self.dummy_head.next
            for i in range(index):
                node = node.next
            return node
        # search from tail, note range should start from size -1
        node = self.dummy_tail.prev
        for i in range(self.size-1, index, -1):
            node = node.prev
        return node

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        try:
            node = self.getNode(index)
            return node.val
        except IndexError:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val, self.dummy_head, self.dummy_head.next)
        self.dummy_head.next.prev = node
        self.dummy_head.next = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val, self.dummy_tail.prev, self.dummy_tail)
        self.dummy_tail.prev.next = node
        self.dummy_tail.prev = node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return

        if index <= 0:
            self.addAtHead(val)
        else:
            inode = self.getNode(index-1)
            node = Node(val, inode, inode.next)
            inode.next.prev = node
            inode.next = node
            self.size +=1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index<0 or index >=self.size:
            return
        inode = self.getNode(index)
        inode.prev.next = inode.next
        inode.next.prev = inode.prev
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.get(0)
# obj.addAtHead(11)
# obj.addAtTail(19)
obj.addAtIndex(1,2)
obj.get(0)
obj.get(1)
obj.addAtIndex(0,1)
obj.get(0)
obj.get(2)
# obj.deleteAtIndex(0)
