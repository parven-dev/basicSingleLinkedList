class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.length = 0
        
        
class SlinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
        if self.head is None:
            node1 = Node(1)
            node2 = Node(2)
            self.head = node1
            self.head.next = node2
            self.tail = node2




slinked_list = SlinkedList()
