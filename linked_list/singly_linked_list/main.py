class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.length = 0
        
        
class SlinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
       

slinked_list = SlinkedList()
node1 = Node()
slinked_list.head =node1
slinked_list.tail = node1
