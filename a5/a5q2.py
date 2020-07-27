# Assignment 5 Question 2
# Jeremy Bernhardt, jrb569, 11119747, CMPT 145: 2020ST2

import node as N
from a5q1 import to_string

def sumnc(node_chain):
    """
    Purpose:
        Given a node chain with numeric data values, calculate 
        the sum of the data values.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty, containing 
                           numeric data values
    Post-condition:
            None
    Return
            :return: the sum of the data values in the node chain
    """

    # Walk list, summing as we go
    cNode = node_chain
    cSum  = 0
    while cNode != None:
        cSum += cNode.get_data()
        cNode = cNode.get_next()

    return cSum

def count_in(node_chain, value):
    """
    Purpose:
        Counts the number of times a value appears in a node chain
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
        :param value: a data value
    Return:
        :return: The number times the value appears in the node chain
    """

    # Walk list
    count = 0
    cNode = node_chain
    while cNode != None:
        #incrementing counter on 
        if cNode.get_data() == value:
            count += 1
        cNode = cNode.get_next()

    return count


def replace_in(node_chain, target, replacement):
    """
    Purpose:
        Replaces each occurrence of the target value with the replacement
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty
        :param target: a value that might appear in the node chain
        :param replacement: the value to replace the target
    Pre-conditions:
        Each occurrence of the target value in the chain is replaced with 
        the replacement value.
    Return:
        None
    """
    # Walk list
    cNode = node_chain
    while cNode != None:
        # Replace value on match
        if cNode.get_data() == target:
            cNode.set_data(replacement)
        cNode = cNode.get_next()

    return None