# Assignment 5 Question 3
# Jeremy Bernhardt, jrb569, 11119747, CMPT 145: 2020ST2

import node as N
from a5q1 import to_string
from node import node


def check_chains(chain1, chain2):
    """
    Purpose:
        Checks 2 node chains.  
           If they are identical (the same objects), 
                returns a string "same chain"
           If they are equal (same data values in the same order), 
                returns a string "same values"
           Otherwise, returns a string "different"
    Pre-conditions:
        :param chain1: a node-chain, possibly empty
        :param chain2: a node-chain, possibly empty
    Post-conditions:
        None
    Return:
        :return: a string
    """

    # Check if both args exist at same address, if so same chain
    #print(chain1 is chain2, to_string(chain1), to_string(chain2))
    if chain1 is chain2:
        return "same chain"

    # Check if content of chains is identical
    if to_string(chain1) == to_string(chain2):
        return "same values"

    return "different"




def copync(node_chain):
    """
    Purpose:
        creates a duplicate of the given node chain
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty
    Post-conditions:
        None
    Return:
        :return: a new node chain, a node-for node copy 
                 of the given one
    """

    # Edge case
    if node_chain == None:
        return None

    # Walk list, populate with inital value
    retList = N.node(node_chain.get_data())
    srcN = node_chain
    dstN = retList
    while srcN != None:
        # Allocate new node, fill 
        newN = N.node(srcN.get_data())
        # Update dst next ptr
        dstN.set_next(newN)
        dstN = newN
        # Walk src ptr ahead
        if srcN != None:
            srcN = srcN.get_next()
    
    # Discard inital node
    return retList.get_next()

def double_up(node_chain):
    """
    Purpose:
        Modifies the node chain so that every node is doubled.
        E.g., given 1 -> 2 -> 3
              changed to 1 -> 1 -> 2 -> 2 -> 3 -> 3
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty

    Post-conditions:
        The chain is modified to have each node repeated once.
    Return:
        None
    """

    cNode = node_chain
    while cNode != None:
        # Get exit address
        nxtNode = cNode.get_next()
        # Alloc new node, set next to exit
        insNode = N.node(cNode.get_data(), nxtNode)
        # Write new address for current Node
        cNode.set_next(insNode)
        # Skip processing to exit node
        cNode = nxtNode

    return None

  