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
        node = Node(value)
        
        if self.head is  None:
            self.head = node
            self.tail = node
        
        else:
            self.tail.next = node
            self.tail = node
        
        self.length+=1
            
    
    def display(self):
        temp = self.head
        count_index = 0
        while temp is not None:
            print(f"index {count_index}: {temp.value} => ",end="")
            temp = temp.next
            count_index+=1
            
    
    def insert_value(self, index, value):
        new_node = Node(value)
        
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        
        else:
            temp = self.head 
            for _ in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length+=1
            
            
            
            
            
            
            
            
            

ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(40)
ll.append(50)
ll.append(60)


print(ll.insert_value(2, 3))

print(ll.display())