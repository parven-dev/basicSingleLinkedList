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
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
            
    
    def reverse(self):
        temp = self.head 
        self.head = self.tail
        self.tail = temp
        
        after =temp.next
        before = None
        length = self.length
        
        for _ in range(length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            
        
            
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.reverse()
ll.display()