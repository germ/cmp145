# Jeremy Bernhardt, jrb569, 11119747, CMPT 145: 2020ST2

import random as rand
import node as N

def to_string(chain):
    """
    Purpose:
        Return a stringified representation of node-chain.
    Pre-conditions:
        :param chain: A node chain
    Return:
        :return: a string
    """

    # Base case, short circuts 
    if chain == None:
        return "EMPTY"

    # Handle populated list recursively
    if chain.next:
        return f"{chain.data} -> {to_string(chain.next)}"
    return f"{chain.data}"


def randchain(n, data_values):
    """
    Purpose:
        Create a random chain selecting n values from the given data_values
    Pre-conditions:
        :param n: an integer >= 0
        :param data_values: a Python list of values to be used as data
    Return:
        :return: a node chain, exactly n nodes in length
                 containing values chosen at random from data_values
    """
    # Base case
    if len(data_values) == 0 or n == 0:
        return None

    # Reorginize the list, pass slice to further invocations
    rand.shuffle(data_values)
    return N.Node(data_values[-1], randchain(n-1, data_values[:-1]))