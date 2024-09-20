
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
            
  
    
    
    def find_kth_node(self, k ):
        slow = self.head
        fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            else:
                fast = fast.next
        print(fast.value, "fast node")
        while fast:
            slow = slow.next
            fast = fast.next
        
        return slow.value
            
            
        
            
    def display(self):
        temp = self.head 
        print(self.length)
        
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
            
            
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.append(60)

print(ll.find_kth_node(5))

        