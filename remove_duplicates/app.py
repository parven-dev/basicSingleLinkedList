class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        

    def append(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head  = new_node
            self.tail = new_node
            
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
            
    def remove_duplicates(self):
        values = set()
        previous = None
        current = self.head
        
        while current:
            previous.next = current.next 
            self.length -= 1
            
        else:
            values.add(current.value)
            previous = current
            
        current = current.next
      
                
        
        
            
    def display(self):
        temp = self.head 
        print(self.length)
        
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
            
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(10)
ll.append(30)

ll.remove_duplicates()
ll.display()
        