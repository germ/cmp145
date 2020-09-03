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
        # Handly empty list
        if self.is_empty():
            return (False, None)

        # Store data, update structure
        nRet = self._head
        self._head = nRet.next

        # Update struct
        self._size -= 1

        # Fix tail
        if self._size <= 1:
            self._tail = self._head

        return (True, nRet.data)
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

        # cache last val
        retVal = self._tail

        # Handle start of list operations
        if self._size == 2:
            self._tail = self._head
            self._size -= 1
            return (True, retVal.data)
        if self._size == 1:
            self._head = None
            self._tail = None
            self._size -= 1
            return (True, retVal.data)

        # Iterate through list to find second to last elem
        pNode = self._head
        cNode = self._head
        while cNode.next != None:
            pNode = cNode
            cNode = cNode.next

        # Modify the list
        pNode.next = None
        self._tail = pNode
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
    def retrieve_data_at_index(self, idx):
        """
        Purpose
            Get the data from node idx in the list
        Preconditions:
            :param idx: The index to return
        Post-Conditions:
            none
        Return
            :return Tuple (True, val), where val is the data value stored at indexidx.
            :return Tuple (False, None), if idx is not valid for the list
        """
        # Handle empty list
        if self.is_empty():
            return (False, None)

        # Check validity of idx
        if idx > self.size() or idx < 0:
            return (False, None)

        # Iterate to idx
        i = 0
        cNode = self._head
        while cNode != None:
            if idx == i:
                return (True, cNode.data)
            i += 1
            cNode = cNode.next
        
        # In theory we should never get here
        return (False, None)
    def set_data_at_index(self, idx, val):
        """
        Purpose
            Set the value of node at idx to val
        Preconditions
            :param idx: Offset of node to be modified
            :param val: value that will overwrite original data
        Post-Conditions
            node idx's value is changed to val
        Return
            :return True,  if value was changed
            :return False, if value was unable to be set
        """
        # Handle empty list
        if self.is_empty():
            return False

        # Check validity of idx
        if idx > self.size() or idx < 0:
            return False

        # Iterate to idx
        i = 0
        cNode = self._head
        while cNode != None:
            if idx == i:
                cNode.data = val
                return True
            i += 1
            cNode = cNode.next
        
        # In theory we should never get here
        return False
    def insert_value_at_index(self, val, idx):
        """
        Purpose
            Insert the data value val into the linked list object at index idx
        Preconditions
            :param val: value that will be inserted 
            :param idx: Location where new node will exist in list
        Post-Conditions
            A node is inserted into the list at idx
        Return
            :return True,  if value was added sucessfully
            :return False, otherwise 
        """
        # Handle empty list
        if self.is_empty() or idx == 0:
            self.add_to_front(val)
            return True
        elif idx == self._size:
            self.add_to_back(val)
            return True

        # Check validity of idx
        if idx > self.size() or idx < 0:
            return False

        # Iterate to idx
        i = 0
        pNode = self._head
        cNode = self._head
        while pNode != None:
            # Preform the insert
            if idx == i:
                nIns = node(val, cNode)
                pNode.next = nIns

                # Handle updating struct
                if self._size == 1:
                    self._tail = nIns
                self._size += 1

                return True
            i += 1
            pNode = cNode
            cNode = cNode.next
        
        # In theory we should never get here
        return False
    def delete_item_at_index(self, idx):
        """
        Purpose
            Delete the node at index idx in the list
        Preconditions
            :param idx: location of node
        Post-Conditions
            The node at idx will be removed from the list
        Return
            :return True,  if value was deleted sucessfully
            :return False, otherwise 
        """
        # Handle clear
        if self._size == 1:
            self._head = None
            self._tail = None
            self._size = 0
            return True

        # Handle front/rear
        if idx == 0:
            return self.remove_from_front()[0]
        if idx+1 == self._size:
            return self.remove_from_back()[0]

        # Iterate to idx
        i = 0
        pNode = self._head
        cNode = self._head
        while pNode != None:
            # Preform the insert
            if idx == i:
                pNode.next = cNode.next
                self._size -= 1
                return True
            i += 1
            pNode = cNode
            cNode = cNode.next
        
        # In theory we should never get here
        return False

    def printList(self):
        cNode = self._head
        while cNode != None:
            print(cNode.data)
            cNode = cNode.next