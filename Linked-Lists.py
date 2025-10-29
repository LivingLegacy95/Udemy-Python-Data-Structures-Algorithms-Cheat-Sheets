
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
        if self.head is None:                           # edge case: if list.is_empty
            self.head = new_node
            self.tail = new_node
        else:                                           # edge case: if there is already nodes in the linked list
            self.tail.next = new_node                   # pointing self.tail at the new node    
            self.tail = new_node                        # assigning self.tail to the newly appended node
        self.length += 1                                # incrementing the length of the list
        return True
    
        # The `prepend` function adds a new node with a given value to the beginning of a linked list.
        # :param value: The `prepend` method you provided is used to add a new node with the given value
        # at the beginning of a linked list. The `value` parameter represents the data that will be stored
        # in the new node being added to the linked list
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:                            # edge case: if list.is_empty
            self.head = new_node                        # pointing and assigning self.head and self.tail to the new node
            self.tail = new_node
        else:
            new_node.next = self.head                   # this line points the new node at the current self.head of the linked list 
            self.head = new_node                        # assigns the head of the linked list to the new node
        self.length += 1                                # increasing the length of the list to reflect prepended node
        return True
    
        # The code `if self.length == 0: return None` is a condition check in the `pop` method of the
        # `LinkedList` class. It is checking if the linked list is empty (i.e., its length is 0). If
        # the linked list is empty, it returns `None` indicating that there are no elements to pop
        # from the list. This is a common practice to handle edge cases and prevent errors when trying
        # to pop elements from an empty list.
    def pop(self):
        if self.length == 0:                            # edge case: if list.is_empty
            return None
        temp = self.head                                # variable to store value of the current index while iterating through linked list
        previous = self.head                            # variable to store value of the previous index while iterating through linked list
        while temp.next is not None:                    # while there are still items in the linked list
            previous = temp                             # sets 'previous' variable to whatever 'temp' is while iterating through the list.
            temp = temp.next                            # logic to iterate through the linked list. 'temp' is being assigned to the next index of the list
        self.tail = previous                            # when loop has finished 'self.tail' is set to the last item of the list 
        self.tail.next = None                           # setting the value of the next item of the last index of the linked list to none to delete popped node
        self.length -= 1                                # decreasing the list by one to reflect poppped node
        if self.length == 0:                            # edge case: if list.is_empty
            self.head = None
            self.tail = None
        # return temp.value                             # this function return the memory address of the object, to see the value of that object, uncomment this line
        return temp
    
        # This Python function removes and returns the first element of a linked list.
        # :return: The `pop_first` method is returning the node that was removed from the beginning of the
        # linked list. If the linked list is empty (length is 0), it will return `None`. Otherwise, it will
        # return the node that was removed.
    def pop_first(self):
        if self.length == 0:                            # edge case: if list.is_empty              
            return None
        temp = self.head                                # assigning a variable to self.head
        self.head = self.head.next                      # pointing self.head to the next node
        temp.next = None                                # this line removes the original self.head node by assigning the next node to none which effectively pops node off the list
        self.length -= 1                                # decreasing the list to reflect poppped node
        if self.length == 0:                            
            self.tail = None                            
        return temp
        # return temp.value                             # this function return the memory address of the object, to see the value of that object, uncomment this line

        # This function retrieves the node at a specified index in a linked list.
        
        # :param index: The `index` parameter in the `get` method is used to specify the position of the node
        # that you want to retrieve from the linked list. It represents the index of the node starting from 0
        # for the head node
        # :return: The code is returning the node at the specified index in a linked list.
    def get(self, index):
        if index < 0 or index >= self.length:           # edge case: testing for if index is called outside of the linked list
            return None
        temp = self.head                                # assigning a variable to current self.head node
        for _ in range(index):                          # for loop to iterate through linked list
            temp = temp.next                            # this line iterates through the linked list until the index parameter that was called has been met
            return temp
    
        # The `set_value` function updates the value at a specified index in a data structure if the index
        # exists.
        # :param index: The `index` parameter in the `set_value` method refers to the position or key in the
        # data structure where you want to set a new value
        # :param value: The `value` parameter in the `set_value` method represents the new value that you want
        # to assign to the node at the specified index in the data structure
        # :return: The `set_value` method returns `True` if the value at the specified index is successfully
        # updated, and `False` if the index does not exist in the data structure (i.e., the `get` method
        # returns `None` for that index).
    def set_value(self, index, value):
        temp = self.get(index)                           # using previous method to call index given as arguement
        if temp:                                         # = if temp is not None, meaning whenever you call for an index in the arguement there has to be a value at that index
            temp.value = value                           # assigning the value of the variable assigned to the index you called as the 'value' defined in the arguement                   
            return True
        return False
    
        # The insert function adds a new node with a specified value at a given index in a linked list.
        
        # :param index: The `index` parameter in the `insert` method refers to the position at which you want
        # to insert a new value in the linked list. It represents the index where the new value should be
        # inserted
        # :param value: The `value` parameter in the `insert` method represents the value that you want to
        # insert into the linked list at a specific index. This value will be stored in a new node and
        # inserted at the specified index in the linked list
        # :return: The `insert` method returns a boolean value - `True` if the insertion was successful, and
        # `False` if the index is out of bounds.
    def insert(self, index, value):
        if index < 0 or index >= self.length:            # edge case: testing for if index is called outside of the linked list
            return False
        if index == 0:                                   # edge case: if list.is_empty prepend the 'value' of the arguement given
            return self.prepend(value)
        if index == self.length:                         # edge case: adding new node to the back of the linked list
            return self.append(value)
        new_node = Node(value)                           # instantiating a new node
        temp = self.get(index -1)                        # edge case: inserting a new node in the middle of the linked list   
        new_node.next = temp.next                        # points to the next node in the linked list, new_node.next and temp.next are now pointing at the same node
        temp.next = new_node                             # points temp at the new node adding it to the list    
        self.length += 1                                 # increasing linked list length to reflect added node
        return True
    
        # This Python function removes a node at a specified index from a linked list.
        
        # :param index: The `remove` method you provided seems to be a part of a linked list implementation.
        # The `index` parameter in this method represents the position of the node that needs to be removed
        # from the linked list
        # :return: The code snippet provided is a method for removing a node at a specific index in a linked
        # list. The method returns the node that was removed from the linked list.
    def remove(self, index):
        if index < 0 or index >= self.length:           # edge case: testing for if index is called outside of the linked list
            return None
        if index == 0:                                  # edge case: if linked list.is_empty pop the first node using the 'pop_first" method and return the value of that index
            return self.pop_first()
        if index == self.length - 1:                    # edge case: if removing the last node of the linked list
            return self.pop()
        prev = self.get(index - 1)                      # edge case: grabbing a node by the index from within the middle of the list
        temp = prev.next                                # O(n) logic to grab the next node of the index you got from the .get() method. O(1) would be temp = self.get(index -1)
        prev.next  = temp.next                          # points the current grabbed node at the node next to the temp node
        temp.next = None                                # pointing temp.next to nothing which removes this node from the list
        self.length -= 1                                # decreasing linked list length by 1 to reflect popped node
        return temp
    
        # This Python function reverses a linked list by swapping the head and tail nodes and updating the
        # next pointers accordingly.
    def reverse(self):
        temp = self.head                                # assigning a variable to the head of the linked list
        self.head = self.tail                           # points head of the linked list at the last node of the linked list
        self.tail = temp                                # points the self.tail variable to the variable that was assigned to the self.head of the linked list
        after = temp.next                               # this variable is assigned to the node after the beginning node of the list
        before = None                                   # this variable is assigned to the node before the beginning node of the list
        for _ in range(self.length):                    # for loop to iterate through the linked list
            after = temp.next                           # points the 'after' node to the node set before the 'after' node variable that was assigned as 'temp'
            temp.next = before                          # points the 'temp' node to the node set before the 'temp' node variable that was assigned to 'before'
            before = temp                               # 'before' node now slides over to the right
            temp = after                                # 'temp' node slides over to the right


#                                                                                            # ***Interview Questions*** # 

# Implement the find_middle_node method for the LinkedList class.
# Note: this LinkedList implementation does not have a length member variable.
# If the linked list has an even number of nodes, return the first node of the second half of the list.
# Keep in mind the following requirements:
    # The method should use a two-pointer approach, where one pointer (slow) moves one node at a time and the other pointer (fast) moves two nodes at a time.
    # When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the middle node of the list.
    # The method should return the middle node when the number of nodes is odd or the first node of the second half of the list if the list has an even number of nodes.
    # The method should only traverse the linked list once.  In other words, you can only use one loop.
    def find_middle_node(self):
        slow = self.head                                # assigning a variable to head of the linked list
        fast = self.head                                # assigning a variable to head of the linked list
        while fast is not None and fast.next is not None: # this parameter is checking for when the index value have moved outside the length of the list
            slow = slow.next                            # iterating through linked list one step at a time
            fast = fast.next.next                       # iterating through linked list two steps at a time
        return slow

# LL: Has Loop ( ** Interview Question)

# Write a method called has_loop that is part of the linked list class.
# The method should be able to detect if there is a cycle or loop present in the linked list.
# You are required to use Floyd's cycle-finding algorithm (also known as the "tortoise and the hare" algorithm) to detect the loop.
# This algorithm uses two pointers: a slow pointer and a fast pointer. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If there is a loop in the linked list, the two pointers will eventually meet at some point. If there is no loop, the fast pointer will reach the end of the list.
# The method should follow these guidelines:
    # Create two pointers, slow and fast, both initially pointing to the head of the linked list.
    # Traverse the list with the slow pointer moving one step at a time, while the fast pointer moves two steps at a time.
    # If there is a loop in the list, the fast pointer will eventually meet the slow pointer. If this occurs, the method should return True.
    # If the fast pointer reaches the end of the list or encounters a None value, it means there is no loop in the list. In this case, the method should return False.
    # If your Linked List contains a loop, it indicates a flaw in its implementation. This situation can manifest in several ways:
def has_loop(self):
    slow = self.head                                # assigning a variable to head of the linked list
    fast = self.head                                # assigning a variable to head of the linked list
    while fast is not None and fast.next is not None: # this parameter is checking for when the index value have moved outside the length of the list
        slow = slow.next                            # iterating through linked list one step at a time
        fast = fast.next.next                       # iterating through linked list two step at a time
        if slow == fast:                            # checking to see if slow ever equals fast or "catches" up to fast meaning there was a loop. Returns true.
            return True
    return False                                    # returns false when loop is finished and slow =! fast



# LL: Find Kth Node From End ( ** Interview Question)
# Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input, and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.
# NOTE: This is a SEPARATE FUNCTION that is NOT a method within the LinkedList class.  This means you need to indent the function all the way to the LEFT. 
# Given this LinkedList:
# 1 -> 2 -> 3 -> 4 -> 5
# If k=1 then return the first node from the end (the last node) which contains the value of 5.
# If k=2 then return the second node from the end which contains the value of 4, etc.
# If the index is out of bounds, the program should return None.
# The find_kth_from_end function should follow these requirements:    # The function should utilize two pointers, slow and fast, initialized to the head of the linked list.
    # The fast pointer should move k nodes ahead in the list.
    # If the fast pointer becomes None before moving k nodes, the function should return None, as the list is shorter than k nodes.
    # The slow and fast pointers should then move forward in the list at the same time until the fast pointer reaches the end of the list.
    # The function should return the slow pointer, which will be at the k-th position from the end of the list.
def find_kth_from_end(ll, k):       
    slow = ll.head                              # assigning a variable to head of the linked list
    fast = ll.head                              # assigning a variable to head of the linked list
    for _ in range(k):
        if fast is None:                        # edge case: if index is outside of ll range
            return None
        fast = fast.next
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow



# LL: Remove Duplicates ( ** Interview Question)

# You are given a singly linked list that contains integer values, where some of these values may be duplicated.
# Note: this linked list class does NOT have a tail which will make this method easier to implement.
# Your task is to implement a method called remove_duplicates() within the LinkedList class that removes all duplicate values from the list.
# Your method should not create a new list, but rather modify the existing list in-place, preserving the relative order of the nodes.
# You can implement the remove_duplicates() method in two different ways:
# Using a Set - This approach will have a time complexity of O(n), where n is the number of nodes in the linked list. You are allowed to use the provided Set data structure in your implementation.
# Without using a Set - This approach will have a time complexity of O(n^2), where n is the number of nodes in the linked list. You are not allowed to use any additional data structures for this implementation.
# Here is the method signature you need to implement:
# def remove_duplicates(self):
# Example:
# Input:
# LinkedList: 1 -> 2 -> 3 -> 1 -> 4 -> 2 -> 5
# Output:
# LinkedList: 1 -> 2 -> 3 -> 4 -> 5

# (****On^2 method)
def remove_duplicates(self):
        current = self.head
        while current is not None:
            runner = current
            while runner.next is not None:
                if runner.next.value == current.value:
                    runner.next = runner.next.next
                    self.length -= 1
                else:
                    runner = runner.next
            current = current.next

# (***O(n) method)
def remove_duplicates(self):
        values = set()
        previous = None
        current = self.head
        while current is not None:
            if current.value in values:
                previous.next = current.next
                self.length -= 1
            else:
                values.add(current.value)
                previous = current
            current = current.next








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
my_linked_list.insert(2, 32)
my_linked_list.remove(3)

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
