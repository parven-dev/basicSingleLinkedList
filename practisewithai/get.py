class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 1

    def append(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node

    
    def prepend(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def get(self, index):
        if index <  0 or index  >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        
            return temp.data


    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    
            
            


ll = LinkedList()
ll.append(2)
ll.append(4)
ll.prepend(1)


print(ll.get(4), "this is i get rn")



