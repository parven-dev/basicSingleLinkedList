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
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length+=1
            
    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        
        if index == 0:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -=1
        
        else:
            temp = self.head
            pre = self.head
            for _ in range(index):
                pre =  temp
                temp = temp.next
            
            pre.next = temp.next
            temp.next = None
            self.length -= 1
           
           
            
                
    
    
    
    def display(self):
        temp = self.head
        
        while temp is not None:
            print(temp.value)
            temp = temp.next
            


ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
print(ll.remove(0))
ll.display()
