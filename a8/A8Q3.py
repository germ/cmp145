# Jeremy Bernhardt, jrb569, 11119747, CMPT 145: 2020ST2

from A8Q2 import insert_node
from A8Q1 import to_string

def split_chain(pivot, chain):
    """
    Purpose:
        Return a tuple of three node-chains (lc, ec, gc)
            lc: all nodes with data values less than the pivot value
            ec: all nodes with data values equal to the pivot value
            gc: all nodes with data values greater than the pivot value
    Pre-conditions:
        :param pivot: A numerica value
        :param chain: A node chain of any length
    Post-conditions:
        The nodes in the chain are re-organized!
    Return:
        :return: a tuple with three node chains
    """
    # Empty list
    if not chain:
        return (None, None, None)
    # Last element, bubble up
    elif chain.next == None:
        if   chain.data < pivot:
            return (chain, None, None)
        elif chain.data > pivot:
            return (None, None, chain)
        elif chain.data == pivot:
            return (None, chain, None)
    # Elems remaining, recurse
    else:
        # Get sorted lists
        nRef = chain.next
        chain.next = None
        ll, el, gl = split_chain(pivot, nRef)
        if   chain.data < pivot:
            return (insert_node(chain, ll), el, gl)
        elif chain.data > pivot:
            return (ll, el, insert_node(chain, gl))
        elif chain.data == pivot:
            return (ll, insert_node(chain, el), gl)

def extend_chain(chain1, chain2):
    """
    Purpose:
        Attaches chain2 to the end of chain1.
    Pre-conditions:
        :param chain1: A node chain of any length
        :param chain2: A node chain of any length
    Post-conditions:
        The nodes in the chain are re-organized!
    Return:
        :return: a single node chain will all the nodes from both chains
    """
    # Handle empty chains
    if chain1 and not chain2:
        return chain1
    elif chain2 and not chain1:
        return chain2
    elif not chain1 and not chain2:
        return None

    # Get to end of l1 for operation
    elif chain1.next:
        extend_chain(chain1.next, chain2)
    else:
        chain1.next = chain2

    # Return ptr
    return chain1

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
    # Handle empty chain
    if not chain:
        return None

    # Split along pivot
    ll, el, gl = split_chain(chain.data, chain)
    # Recurse for sublists
    if ll and ll.next:
        ll = sort_chain(ll)

    if gl and gl.next:
        gl = sort_chain(gl)

    # zip result
    return extend_chain(extend_chain(ll, el), gl)