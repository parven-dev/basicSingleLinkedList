class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class SlinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

        
    
    def insert(self, value, location):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1 
        
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                
            elif location == -1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            
            else:
                temp = self.head
                index = 0
                
                while index < location -1:
                    temp = temp.next
                    index += 1
                nextNode = temp.next
                temp.next = new_node
                new_node.next = nextNode
            
                
    
    def display(self):
        temp = self.head
        
        while temp is not None:
            print(temp.value, "en")
            temp = temp.next
        
        

slinked_list = SlinkedList()


slinked_list.insert(2, 0)
slinked_list.insert(2, 0)
slinked_list.insert(1, -1)
slinked_list.insert(4, 0)
slinked_list.insert(8, 4)



print(slinked_list.display())
