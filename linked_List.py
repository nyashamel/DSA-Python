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
        current= new_nodeA

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

#DOUBLY LINKED LISTS 

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None 

    def insert_at_end(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
    def display_forward(self):
            current = self.head

            if not current:
                print ("List is empty")
                return
            while current:
                print(current.data, end= "=>")
                current = current.next
            print ("None")
    def display_backward(self):
            current = self.head

            if not current:
                print("List is empty")
                return
            while current:
                print(current.data, end="=>")
                current =current.prev
            print("None")

    def delete_by_value(self, value):
            current = self.head
            if current and current.data == value:
                if not current.next:
                    self.head = None
                else:
                    self.head = current.next
                    self.head.prev = None
                current = None
                return
            
            while current and current.data != value:
                current = current.next

            if not current:
                print ("Value nit found in List")
                return
            
            if current.next:
                current.next.prev = current.prev
            if current.prev:
                current.prev.next = current.next
            current = None

dll= DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(2)
dll.insert_at_end(4)

print("Doubly Linked List (Forward):")
dll.display_forward()

print("Doubly Linked List (Backward):")
dll.display_backward()

print("Deleting a node with value 20:")
dll.delete_by_value(20)
dll.display_forward()

#SUM OF A TWO DIMENSIONAL ARRAY
def sum_of_2D_array(array):
    total_sum =0
    for row in array:
        for num in row:
            total_sum += num
    return total_sum

array = [
    [1,2,3],
    [8,7,6],
    [4,5,6]
]

result= sum_of_2D_array(array)
print("The sum of all umbers in the 2D array is:", result)


#Implementation of Stack Using a Linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  
class Stack:
    def __init__(self):
        self.top = None 

    def push(self, data):
        """Add an element to the top of the stack."""
        new_node = Node(data)
        new_node.next = self.top 
        self.top = new_node  

    def pop(self):
        """Remove and return the element from the top of the stack."""
        if self.is_empty():
            print("Stack is empty!")
            return None
        popped_data = self.top.data  
        self.top = self.top.next  
        return popped_data

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.top.data

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

    def display(self):
        """Display all elements in the stack."""
        if self.is_empty():
            print("Stack is empty!")
            return
        current = self.top
        print("Stack elements (Top to Bottom):")
        while current:
            print(current.data, end=" => ")
            current = current.next
        print("None")

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)


stack.display()

print("Top element is:", stack.peek())


print("Popped element:", stack.pop())
stack.display()

print("Popped element:", stack.pop())
print("Popped element:", stack.pop())


print("Popped element:", stack.pop())

        
class Stack:
    def __init__(self, size):
        """Initialize the stack with a fixed size."""
        self.stack = []  # Array to store stack elements
        self.size = size  # Maximum size of the stack

    def push(self, data):
        """Add an element to the top of the stack."""
        if len(self.stack) >= self.size:
            print("Stack Overflow! Cannot add more elements.")
        else:
            self.stack.append(data)
            print(f"Pushed {data} onto the stack.")

    def pop(self):
        """Remove and return the top element from the stack."""
        if self.is_empty():
            print("Stack Underflow! The stack is empty.")
            return None
        return self.stack.pop()

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.stack[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def display(self):
        """Display all elements in the stack."""
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack elements (Top to Bottom):")
            for i in reversed(self.stack):
                print(i, end=" => ")
            print("None")

stack = Stack(size=5)  
stack.push(10)
stack.push(20)
stack.push(30)

stack.display()


print("Top element is:", stack.peek())


print("Popped element:", stack.pop())
stack.display()


stack.pop()
stack.pop()
stack.pop()  
