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
                current = current.next
        current= new_node

    def display (self):
        current = self.head
        if not current:
            print("list is empty")
            return
        while current:
            print (current.data, end= "=>")
            current = current.next
        print(None)

    def deleted_by_value(self, value):
        current = self.head

        if current and current.data == value:
            self.head = current.next
            current = None
            return
        
        prev = None
        while current and current.data != value:
            prev =current 
            current = current.next

        if not current:
            print("value not found in list")
            return
        
        prev.next = current.next
        current= None 

llist = LinkedList()
llist.insert_at_end(10)
llist.insert_at_end(1)
llist.insert_at_end(9)
llist.insert_at_end(5)
print("Linked List:")
llist.display()

print("Deleting a node with value 1")
llist.deleted_by_value(1)
llist.display()

# Fibonacci Series

def fib_iterative(n):
    fib_series =[]
    a, b = 0, 1

    for _ in range (n):
        fib_series.append (a)
        a,b = b, a+b

    return fib_series

print(fib_iterative(10))

#FACTORIAL OF A NUMBER

def factorial_ite(n):
    result = 1 
    for i in range (1, n +1):
        result *= i
    return result
print(factorial_ite)
