# Jeremy Bernhardt, jrb569, 11119747, CMPT 145: 2020ST2

class node(object):
    """ A version of the Node class with public attributes.
        This makes the use of node objects a bit more convenient for 
        implementing LList class.  
        
        Since there are no setters and getters, we use the attributes directly.
        
        This is safe because the node class is defined in this module.  
        No one else will use this version of the class.  
    """

    def __init__(self, data, next=None):
        """
        Create a new node for the given data.
        Pre-conditions:
            data:  Any data value to be stored in the node
            next:  Another node (or None, by default)
        """
        self.data = data
        self.next = next
    
    # Note: use the attributes directly; no setters or getters!


class LList(object):
    def __init__(self):
        """
        Purpose
            creates an empty list
        """
        self._size = 0     # how many elements in the stack
        self._head = None  # the node chain starts here; initially empty
        self._tail = None  # the last node in the node chain; initially empty


    def is_empty(self):
        """
        Purpose
            Checks if the given list has no data in it
        Return:
            :return True if the list has no data, or False otherwise
        """
        # Check size attr
        if self._size == 0:
            return True
        return False

    def size(self):
        """
        Purpose
            Returns the number of data values in the given list
        Return:
            :return The number of data values in the list
        """
        return self._size

    def add_to_front(self, val):
        """
        Purpose
            Insert val at the front of the node chain
        Preconditions:
            :param val:   a value of any kind
        Post-conditions:
            The list increases in size.
            The new value is at index 0.
            The values previously in the list appear after the new value.
        Return:
            :return None
        """
        # Create new node, set head
        self._head = node(val, self._head)

        # Set tail if new list
        if self.size() == 0:
            self._tail = self._head

        # Increase size
        self._size += 1

    def add_to_back(self, val):
        """
        Purpose
            Insert val at the end of the node chain
        Preconditions:
            :param val:   a value of any kind
        Post-conditions:
            The list increases in size.
            The new value is last in the list.
        Return:
            :return None
        """
        # Handle add to empty list
        if self.size() == 0:
            self._head = node(val)
            self._tail = self._head
        # Insert node, update ptrs
        else:
            self._tail.next = node(val)
            self._tail = self._tail.next

        # Increment counter
        self._size += 1

    def remove_from_front(self):
        """
        Purpose
            Removes and returns the first value 
        Post-conditions:
            The list decreases in size.
            The returned value is no longer in in the list.
        Return:
            :return The pair (True, value) if self is not empty
            :return The pair (False, None) if self is empty
        """
        nRet = self._head
        self._size -= 1
        self._head = self._head.next

        if self.is_empty():
            return (True, nRet.value)
        return (False, None)



    def remove_from_back(self):
        """
        Purpose
            Removes and returns the last value
        Post-conditions:
            The list decreases in size.
            The returned value is no longer in in the list.
        Return:
            :return The pair True, value if self is not empty
            :return The pair False, None if self is empty
        """

        # Check for populated struct
        if self.is_empty():
            return (False, None)

        # Iterate through list to find second to last elem
        pNode = self._head
        cNode = self._head
        while cNode != None:
            pNode = cNode
            cNode = cNode.next

        # Modify the list
        pNode.next = None
        self._size -= 1

        return (True, pNode.data)

    def value_is_in(self, val):
        """
        Purpose
            Check if the given value is in the list
        Preconditions:
            :param val:   a value of any kind
        Post-conditions:
            none
        Return:
            :return True if the value is in the list, False otherwise
            :return (False if the list is empty)
        """
        # Check for populated list
        if self.is_empty():
            return False

        # Iterate over list
        cNode = self._head
        while cNode != None:
            # Break out if found
            if cNode.data== val:
                return True
            cNode = cNode.next
        
        # Not found in list
        return False


    def get_index_of_value(self, val):
        """
        Purpose
            Return the smallest index of the given val.
        Preconditions:
            :param val:   a value of any kind
        Post-conditions:
            none
        Return:
            :return True, idx if the val appears in self
            :return False, None if the value does not appear in self
        """
        # Empty list
        if self.size() == 0:
            return (False, None)

        # Iterate through list, break on end of list or match found
        cNode = self._head
        for i in range(0, self.size()):
            # End of list, no value found
            if cNode == None:
                return (False, None)
            
            # Found a match
            if cNode.data == val:
                return (True, i)
            
            # Advance ptr
            cNode = cNode.next
        
        return (False, None)