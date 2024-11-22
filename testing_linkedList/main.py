class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Linked_list():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self,value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length+=1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.next = self.head
            self.head = new_node
            
            self.length +=1
            
    def insert(self, location, value):
            new_node = Node(value)
            if location < 0 or location > self.length:
                return "Location Must be a non_negative interger"
            
            elif location == 0:
                return self.prepend(value)
            
            elif location == self.length:
                return self.append(value)
            
            index = 0
            temp = self.head
            
            while temp is not None and index < location:
                temp = temp.next
                index +=1 
            print(temp.value, "value found")
            new_node.next = temp.next
            temp.next = new_node
           
    def pop(self):
        if self.length == 0:
            return "there is no node to delete"
        
        temp = self.head
        pre = temp
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        
        
        print(temp.value, "its poped value")
            
    
    def pop_fist(self):
        
        if self.length == 0:
            return None
        temp  = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        
        if self.length == 0:
            self.tail = None
            
        return temp.value
        
    def get(self, index):
        
        if index == -1 or index > self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        print(temp.value, "that value i was looking for")
        return temp
        
    
    def set(self, value, index):
        
        if index < 0 or index > self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        
        temp.value  = value        
        print(temp.value, "set this value")
            
    
    def remove(self, index):
        pre = self.get(index-1)
        temp = self.get(index)
        
        pre.next = temp.next
        temp.next = None

        self.length -= 1


        print("pre", pre.value, "temp", temp.value, "it has to be removed")
        
        
        
        
        
               
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.value, "--> ", end="")
            temp = temp.next

        

            
            
            


l1 = Linked_list(40)
l1.append(39)
l1.append(34)
# l1.append(399)
# l1.prepend(90)
# l1.prepend(50)
# l1.append(20)
l1.insert(0, 555)
l1.insert(4, 543)
l1.insert(5, 200)
l1.insert(10, 200)
print(l1.display())
l1.get(7)
l1.set(100,4)



l1.pop()

l1.pop_fist()
print("after poping")
l1.remove(2)

print(l1.display())

