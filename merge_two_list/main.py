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
            self.tail.next =new_node
            self.tail = new_node
            
        self.length+=1  
        
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def merg_sort(self):
        temp = LinkedList()
        current =  None
   
                    
  
            
        
d1 = LinkedList()
d1.append(40)
d1.append(70)
d1.append(60)
d1.append(50)

# d2 = LinkedList()
# d2.append(10)
# d2.append(80)
# d2.append(30)
# d2.append(20)

d1.display()

# print(d2.display())


# print(d1.display())
