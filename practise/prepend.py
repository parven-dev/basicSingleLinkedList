class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node    
        self.length = 1


    def print_linkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
   

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True   
    
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.next = new_node

ll = LinkedList(5)
ll.append(3)
ll.append(6)

ll.prepend(2)


ll.print_linkedList()