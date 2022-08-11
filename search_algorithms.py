# Represents a node of the list
class Node():

    def __init__(self, value):
        self.value = value
        self.visited = bool
        self.next = None

# Represents the linked list
class LinkedList:

    def __init(self):
        self.head = None
        self.tail = None

    # If the list is empty (self.head is None), return True
    # Else (self.head is not None), return False
    def is_empty(self):
        return not self.head

    # Add a new node to the end of the linked list 
    def enqueue(self, new_node):
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
    # Remove the first node of the linked list 
    # If the linked list is empty, return a warning message
    def dequeue(self):
        if self.is_empty():
            return "Warning: The queue is empty"
        deleted_element = self.head.value
        self.head = self.head.next
        return deleted_element

    # Return the first node of the linked list
    # If the linked list is empty, return a warning message
    def peek(self):
        if self.is_empty():
            return "Warning: The queue is empty"
        return self.head.value

    