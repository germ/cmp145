# Jeremy Bernhardt, jrb569, 11119747, CMPT 145: 2020ST2

def insert_node(node, chain):
    """
    Purpose:
        Put the given node into the right place in the chain, assuming 
        increasing (numeric) values.
    Pre-conditions:
        :param node: A node object, next must be None
        :param chain: A node chain of any length
    Post-conditions:
        The nodes in the chain are re-organized!
    Return:
        :return: the node chain with node added to the right place
    """
    # End of chain
    if not chain:
        return node
    # Found insertion point
    elif chain.data > node.data:
        node.next = chain
        return node
    # Traverse deeper
    else:
        chain.next = insert_node(node, chain.next)
        return chain

def sort_chain(chain):
    """
    Purpose:
        reorganize the nodes in the chain so that the data values are all increasing
    Pre-conditions:
        :param chain: A node chain
    Post-conditions:
        The nodes in the chain are re-organized!
    Return:
        :return: A node chain with data values increasing
    """

    # Empty list
    if not chain:
        return None
    # Insert element into end of list
    elif chain.next == None:
        return insert_node(chain, None)
    # Cache ptr, recursively call
    else:
        nRef = chain.next
        chain.next = None
        return insert_node(chain, sort_chain(nRef))