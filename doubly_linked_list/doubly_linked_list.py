"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next
        return self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev
        return self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        if self.get_values() is None:
            return 0
        return len(self.get_values())
        

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        if self.head is None:
            self.head = ListNode(value)
            
        else:
            new_head = self.head.insert_before(value)
            self.head = new_head
        

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        to_return = self.head.value
        if self.head is self.tail:
            self.head = None
            self.tail = None
            return to_return
        else:
            self.delete(self.head)
        return to_return




    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if self.tail is None:
            self.tail = ListNode(value)
            self.head = self.tail
        else:
            new_tail = self.tail.insert_after(value)
            self.tail = new_tail
        # pass

    def get_values(self):
        list = []
        current = self.head
        if current is not None:
            while (current.next is not None ):
                list.append(current.value)
                current = current.next
            list.append(current.value)
            return list

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        to_return = self.tail
        if self.head is self.tail:
            self.head = None
            self.tail = None
            return to_return.value
        else:
            self.delete(self.tail)
        return to_return.value


    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        node.prev.next = node.next
        node.prev = self.head.prev
        node.next = self.head
        self.head = node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        old_tail = self.tail
        old_head = self.head
        if len(self.get_values) ==2:
            self.head = old_tail
        self.tail = node
        self.tail.next = old_tail.next
        self.tail.prev = old_tail.prev
        node.next.prev = node.prev
        node.prev = self.tail
        node.next = self.tail.next
        self.tail = node
        if node.prev.prev is None:
            self.head = node.prev

            


    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        if self.head == node:
            self.head = self.head.next
        if self.tail == node:
            self.tail = self.tail.prev
        else:
            # node_return = node
            node.delete()
            # return node_return
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        values = self.get_values()
        return max(values)


# dlll = DoublyLinkedList(ListNode(1))
# print("DLL", dlll.get_values(), len(dlll))
# dlll.add_to_tail(30)
# dlll.add_to_tail(13)
# dlll.add_to_tail(33)

# dll = DoublyLinkedList(ListNode(1))
# print("DLL Values", dll.get_values())

# dll.add_to_tail(3)
# print("DLL Values", dll.get_values())
# # assertEqual(self.dll.head.value, 1)
# # assertEqual(self.dll.tail.value, 3)
# dll.move_to_front(dll.tail)
# print("DLL Values", dll.get_values())

# # assertEqual(self.dll.head.value, 3)
# # assertEqual(self.dll.head.next.value, 1)
# # assertEqual(len(self.dll), 2)
# dll.add_to_head(29)
# print("DLL Values", dll.get_values())

# dll.move_to_front(dll.head.next)
# print("DLL Values", dll.get_values())

# # assertEqual(self.dll.head.value, 3)
# # assertEqual(self.dll.head.next.value, 29)
# assertEqual(len(self.dll), 3)

        # self.dll.add_to_tail(3)
        # self.assertEqual(self.dll.head.value, 1)
        # self.assertEqual(self.dll.tail.value, 3)

        # self.dll.move_to_front(self.dll.tail)
        # self.assertEqual(self.dll.head.value, 3)
        # self.assertEqual(self.dll.head.next.value, 1)
        # self.assertEqual(len(self.dll), 2)

        # self.dll.add_to_head(29)
        # self.dll.move_to_front(self.dll.head.next)
        # self.assertEqual(self.dll.head.value, 3)
        # self.assertEqual(self.dll.head.next.value, 29)
        # self.assertEqual(len(self.dll), 3)
# print("DLL added", dlll.get_values(), len(dlll))

dll = DoublyLinkedList(ListNode(1))
print("DLL Values", dll.get_values())

dll.add_to_head(40)
print("DLL Values", dll.get_values())

# assertEqual(self.dll.tail.value, 1)
# assertEqual(self.dll.head.value, 40)
dll.add_to_head(13)
print("DLL Values", dll.get_values())

dll.move_to_end(dll.head)
print("DLL Values", dll.get_values())

# assertEqual(self.dll.tail.value, 40)
# assertEqual(self.dll.tail.prev.value, 1)
# assertEqual(len(self.dll), 2)

dll.add_to_tail(4)
print("DLL Values", dll.get_values())

# dll.move_to_end(dll.head.next)
print("DLL Values", dll.get_values())

# assertEqual(self.dll.tail.value, 40)
# assertEqual(self.dll.tail.prev.value, 4)
# assertEqual(len(self.dll), 3)