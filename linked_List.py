class Node: 
    def __init__(self,data):
        self.data= data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head

    def insert_at_end(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node

        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def dispaly (self):
        current = self.head

        if not current:
            print ('List is empty')
            return

        while current:
            print(current.data, end= "->")
            current = current.next
            print('None')
            

        
        