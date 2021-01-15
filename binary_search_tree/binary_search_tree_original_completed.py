"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from collections import deque

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
    
#     def __len__(self):
#         return self.storage.get_length()

#     def enqueue(self, value):
#         self.storage.add_to_tail(value)

#     def dequeue(self):
#         if not self.storage.get_length == 0:
#             return self.storage.remove_head()
#         else:
#             return None

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self is None:
            self = BSTNode(value)
        else:
            if value < self.value:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = BSTNode(value)
            else: 
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = BSTNode(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self == None:
            return False
        if target == self.value:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value: # value greater than 'node'
            if self.right:
                return self.right.contains(target)
            else:
                return False
        return False


    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return False
        if self.right:
            return self.right.get_max()
        else:
            
            return self.value


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if not self:
            return False
        # prints out each value
        fn(self.value)
        print(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)










    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        if not self: 
            return False
        if self.left:
            self.left.in_order_print(self)
        print(self.value)
        if self.right:
            self.right.in_order_print(self)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        
        queue = deque()
        queue.append(self)
        while (len(queue) > 0):
            current = queue.popleft()
            print(current.value)
            if current.left: 
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(self)
        while (len(stack) > 0):
            current = stack.pop()
            print(current.value)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right) 

        

        # print(self.value)
        # if not self: 
        #     return False
        # if self.left:
        #     self.left.in_order_print(self)
        # if self.right:
        #     self.right.in_order_print(self)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
