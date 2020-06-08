"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if not len(self.storage) == 0:
            return self.storage.pop(0)
        else:
            return None

class Node: 
    def __init__(self, value, next=None):
        self.value = value
        self.next_node = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, data):
        # Wrap data in node instance
        new_node = Node(data)

        if not self.head and not self.tail:
            # List is empty
            # Update both head and tail to point to new node
            self.head = new_node
            self.tail = new_node
        else:
            # Call set_next with new_node on current tail node
            self.tail.set_next(new_node)
            # update self.tail to point to new last node in ll
            self.tail = new_node

    def remove_tail(self):
        if self.tail is None:
            return None
        # Save tail node's data
        data = self.tail.get_value()
        if self.head is self.tail:
            # set both to be None
            self.head = None
            self.tail = None
        
        else:
            # We must traverse entire LL starting from begin
            while current.get_next() ! self.tail:
                current = current.get_next()
                self.tail = current

        return data

    def remove_head(self):
        if self.head is None:
            return None
        # Save head node's data
        data = self.head.get_value()
        if self.head = self.tail:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.get_next()

        return data

    def contains(self, data):
        if not self.head:
            return False
        current = self.head
        while current is not None:
            if current.get_value() == data:
                return True
            current = current.get_next()
        return False

    def get_max(self):
        if self.head is None:
            return None

        current_max = self_head.get_value()

        current = self.head.get_next()

        if current_max < current.get_value():
            current_max = current.get_value()
        current = current.get_next()

        return current_max