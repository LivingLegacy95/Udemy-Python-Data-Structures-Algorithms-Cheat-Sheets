
# The class Node represents a node in a linked list with a value and a reference to the next node.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# This Python class initializes a linked list with a single node containing a specified value.
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    ### METHODS ###
    
    def print_list(self, value):
        temp = self.head
        while self.head is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        # The `append` function adds a new node with a given value to the end of a linked list.
        
        # :param value: The `value` parameter in the `append` method represents the data that you want to add
        # to the linked list as a new node. This value will be stored in the `Node` object that is created
        # with this value and added to the linked list at the end
        # :return: The `append` method is returning a boolean value `True` to indicate that the operation was
        # successful.
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        # The code `if self.length == 0: return None` is a condition check in the `pop` method of the
        # `LinkedList` class. It is checking if the linked list is empty (i.e., its length is 0). If
        # the linked list is empty, it returns `None` indicating that there are no elements to pop
        # from the list. This is a common practice to handle edge cases and prevent errors when trying
        # to pop elements from an empty list.
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp 
            temp = temp.next
        self.tail.next = None
        self.length -= 1
        self.tail = pre
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    




# `my_linked_list = LinkedList(4)` is creating a new instance of the `LinkedList` class with an
# initial value of 4. This line of code initializes a linked list with a single node containing the
# specified value of 4.
my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.print_list(2)
# (2) Items left in list - Returns 2 node
print(my_linked_list.pop())
# (1) Items left in list - Returns 4 node
print(my_linked_list.pop())
# (0) Items left in list - Returns None
print(my_linked_list.pop())

# The code snippet `print('Head:', my_linked_list.head.value)`, `print('Tail:',
# my_linked_list.tail.value)`, and `print('Length:', my_linked_list.length)` is outputting the values
# of the head node, tail node, and the length of the linked list respectively.
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""
