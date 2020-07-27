# Assignment 5 Question 1
# Jeremy Bernhardt, jrb569, 11119747, CMPT 145: 2020ST2

import node as N

def to_string(node_chain):
    """
    Purpose:
        Create a string representation of the node chain.  E.g.,
        [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
    Pre-conditions:
        :param node_chain:  A node-chain, possibly empty (None)
    Post_conditions:
        None
    Return: A string representation of the nodes.
    """
    # special case: empty node chain
    if node_chain is None:
        return 'EMPTY'

    else:
        # walk along the chain
        walker = node_chain
        value = walker.get_data()
        # print the data
        result = '[ {} |'.format(str(value))
        while walker.get_next() != None:
            walker = walker.get_next()
            value = walker.get_data()
            # represent the next with an arrow-like figure
            result += ' *-]-->[ {} |'.format(str(value))

        # at the end of the chain, use '/'
        result += ' / ]'

    return result

