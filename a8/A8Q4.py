# Jeremy Bernhardt, jrb569, 11119747, CMPT 145: 2020ST2

from A8Q3 import insert_node, extend_chain
from A8Q3 import sort_chain as q3sort

def split_chain(chain):
    """
    Purpose:
        Split the given node chain into 2 roughly equal node-chains.
        Return the two node-chains in a tuple.
        If the length of chain is even, the two halves are exactly equal length.
        If the length is odd, then the first chain is longer than the second by 1 node.
    Pre-conditions:
        :param chain: A node chain
    Post-conditions:
        The nodes in the chain are re-organized!
    Return:
        :return: A tuple (lc, rc) where lc and rc are node chains
    """
    # Empty and singleton list
    if not chain:
        return (None, None)
    if not chain.next:
        return (chain, None)

    # Put into head of new lists
    a = chain
    b = chain.next

    nRef = b.next
    a.next = None
    b.next = None

    # Recurse and zip
    if nRef:
        c,d = split_chain(nRef)
        return (insert_node(a, c), insert_node(b,d))
    else:
        return (a,b)

def merge_chain(chain1, chain2):
    """
    purpose:
        given 2 node chains in order of increasing data values, return 
        a single chain containing all the nodes, in order of increasing data values
    pre-conditions:
        :param chain1: a node chain whose data values are increasing
        :param chain2: a node chain whose data values are increasing
    post-conditions:
        the nodes in the chain are re-organized!
    return:
        :return: a node chain with data values increasing
    """    
    # Use recursive solutions from previous answer
    return q3sort(extend_chain(chain1, chain2))

    # Below here is a implementation that doesn't reuse code
    # Singleton/Empty handling
    if not chain1 and not chain2:
        return None
    if chain1 and not chain2:
        return chain1
    if chain2 and not chain1:
        return chain2

    # Recurse through to find insertion point
    if chain1.next:
        merge_chain(chain1.next, chain2)
    # At insertion site
    else:
        chain1.next = chain2

    # Assignment calls for a unsorted impl, tests need this sorted
    return chain1

def sort_chain(chain):
    """
    purpose:
        reorganize the nodes in the chain so that the data values are all increasing
    pre-conditions:
        :param chain: a node chain
    post-conditions:
        the nodes in the chain are re-organized!
    return:
        :return: a node chain with data values increasing
    """
    # Use recursive solutions from previous answer
    return q3sort(chain)

    # Below here is a implementation that doesn't reuse code
    # Empty case
    if not chain:
        return None
    
    #print(to_string(chain))
    # Split into smaller chunks
    if chain.next and chain.next.next != None:
        a, b = split_chain(chain)
        sort_chain(a)
        sort_chain(b)
        # Use helper merge to 
        if a.data <= b.data:
            chain = a
            chain.next = sort_chain(merge_chain(a.next, b))
        else:
            chain = b
            chain.next = sort_chain(merge_chain(a, b.next))
        return chain
    # Last two nodes
    else:
        # Unset ptrs and swap
        nRef = chain.next
        chain.next = None
        if nRef:
            nRef.next = None
            
        if nRef and nRef.data < chain.data:
            # Order changed, recursive sort
            return merge_chain(nRef, chain)
        else:
            return merge_chain(chain, nRef)