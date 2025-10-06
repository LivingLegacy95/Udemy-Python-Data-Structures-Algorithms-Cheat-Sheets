
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
        temp = self.head                                # setting the 'temp' variable to whatever the value of 'self.head' is 
        while self.head is not None:                    # while loop setting parameter to continue loop until liked list is empty 
            print(temp.value)
            temp = temp.next                            # iterating through the list

        # The `append` function adds a new node with a given value to the end of a linked list.
        # :param value: The `value` parameter in the `append` method represents the data that you want to add
        # to the linked list as a new node. This value will be stored in the `Node` object that is created
        # with this value and added to the linked list at the end
    def append(self, value):
        new_node = Node(value)                          # instantiating a new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
        # The `prepend` function adds a new node with a given value to the beginning of a linked list.
        # :param value: The `prepend` method you provided is used to add a new node with the given value
        # at the beginning of a linked list. The `value` parameter represents the data that will be stored
        # in the new node being added to the linked list
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
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
        previous = self.head
        while temp.next is not None:
            previous = temp 
            temp = temp.next
        self.tail = previous
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        # return temp.value                 # this function return the memory address of the object, to see the value of that object, uncomment this line
        return temp
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
        # return temp.value                # this function return the memory address of the object, to see the value of that object, uncomment this line

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
            return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:                           # = if temp is not None
            temp.value = value
            return True
        return False
        # for _ in range(index):
        #     temp = temp.next
        #     temp = value
        #     return temp
    
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.prepend(value)
        new_node = Node(value)
        temp = self.get(index -1)
        new_node.next = temp.next




# `my_linked_list = LinkedList(4)` is creating a new instance of the `LinkedList` class with an
# initial value of 4. This line of code initializes a linked list with a single node containing the
# specified value of 4.
my_linked_list = LinkedList(4)
my_linked_list.append(8)
my_linked_list.append(23)
my_linked_list.append(21)
my_linked_list.append(0)
my_linked_list.print_list(2)
# (2) Items left in list - Returns 2 node
print(my_linked_list.pop())
# (1) Items left in list - Returns 4 node
print(my_linked_list.pop())
# (0) Items left in list - Returns None
print(my_linked_list.pop())
my_linked_list.prepend(1)
my_linked_list.pop_first()
print(my_linked_list.get(2))
my_linked_list.set_value(2,6)
my_linked_list.print_list

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
