"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stackd:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if len(self.storage) > 0:
            return self.storage.pop(len(self.storage)-1)
        else:
            pass

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_value(self):
        return self.data

    def set_value(self, value):
        self.data = value

    def empty_last_node(self):
        self.data = None
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    # def __str__(self):
    #     return 

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)
    
    def remove_from_head(self):
        
        # if list is empty
        if not self.head:
            return None
        # is not empty
        else:
            value = self.head.get_value()
            # print(value)
            self.head = self.head.get_next()
            return value

    def remove_from_tail(self):
        if self.head == None:
            pass
        elif self.head.get_next() == None:
            value = self.head.get_value()
            # Back To Beginning state
            # self.head.data = None
            self.__init__()
            return value
        else:
            current = self.head
            while current.get_next().get_next() is not None:
                current = current.get_next()
                # drie forward
            # Then ya hit the brakes
            
            value = current.get_next().get_value()
            # Grab the value
            current.set_next(None)
            # Cover your tracks
            return value
    
    def get_list(self):
        array = []
        if self.head is not None:
            current = self.head
            while (current.get_next() is not None and current is not None):
                array.append(current.data)
                current = current.get_next()
            array.append(current.data)
        return array
        
    
    def get_length(self):
        # If head is None then length is zero. 
        if self.head == None:
            return 0
        # Otherwise start at one
        length = 1
        # Count the true nodes
        current = self.head
        while current.get_next() is not None:
            length += 1
            current = current.get_next()
        return length
        

        
# my_list = LinkedList()
# my_list.add(1)
# my_list.add(2)
# my_list.add(3)
# my_list.add(9)
# my_list.add("Hello World")
# my_list.add(3)
# my_list.show_list()
# print(my_list.get_length())
# new_list = LinkedList()
# print(new_list.get_length()) # returns 0 
# new_list.add(3)
# print(new_list.get_length()) # returns 1


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.get_length()

    def push(self, value):
        self.storage.add(value)

    def pop(self):
        if self.storage.get_length() > 0:
            return self.storage.remove_from_tail()
        else:
            pass

    def get_array(self):
        return self.storage.get_list()


# test_list = Stack()
# print("EMPTY LIST", test_list.storage.get_list())
# test_list.push(100)
# test_list.push(101)
# test_list.push(105)
# print("FULL LIST", test_list.storage.get_list())
# test_list.pop()
# # test_list.pop()
# print("Less Full List", test_list.storage.get_list())
# test_list.pop()
# test_list.pop()
# print("Empty again", test_list.storage.get_list())
