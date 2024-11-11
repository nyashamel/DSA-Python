class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node

        else: 
            current = self.head
            while current.next:
                curent = current.next
        current= new_node

    def display (self):
        current = self.head
        if not current:
            print("list is empty")
        while current:
            print (self.data, end= "=>")
            current = current.next
        print(None)