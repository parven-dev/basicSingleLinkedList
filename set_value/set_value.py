
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LikedList:
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
            self.tail.next = node # update tail to new node
            self.tail = node

        self.length+=1
    
    def prepend(self, value):
        node = Node(value)
        
        if self.head is None:
            self.head = node
            self.tail = node
        
        else:
            node.next = self.head
            self.head = node
            
            
        self.length+=1
    
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def get_index(self, index):
        if index < 0 or index >= self.length:
            return None
        
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            
        return temp.value
    
    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            
            temp.value = value                  

ll = LikedList()
ll.append(10)
ll.append(20)

ll.prepend(2)
# print(ll.get_index(-1))
print(ll.set_value(2, 30))
print(ll.display())
       