
class  Node:
    def __init__(self, value):
        self.value = value
        self.next = None # pointing to next value if its none it will stop




class SingleLinkeList: # we are creating this class that we are link or add more nodes to link
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("link list is empty")
            return 
        else:
            temp = self.head
            while temp:
                print(temp.value)
                temp = temp.next
        



linkList = SingleLinkeList()
node1 = Node(10)
linkList.head=node1
linkList.display()


        







        