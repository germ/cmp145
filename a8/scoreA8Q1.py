# CMPT 145 Course material
# Copyright (c) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this
# file to a public or private website, or providing this file to a person
# not registered in CMPT 145, constitutes Academic Misconduct, according
# to the University of Saskatchewan Policy on Academic Misconduct.
#
# Synopsis:
#     scoring script for A8Q1
#     student version
#
#     Run this script to see how many of your functions work!
#     

import node as N
import A8Q1 as A8

verbose = True # change to False to reduce output

##### THIS DOES THE WORK
def runemall():
    # a simple script to try all the tests
    count = 0
    passed = 0
    failed = 0
    for t in all_of_em:
        print('Passed:', passed, 'test out of', count)
        count += 1
        try:
            # try calling the function t
            t()
            passed += 1
        except Exception as e:
            # something went wrong in the function call t()
            if verbose:
                print("Test failure in function:", t.__name__)
                print(e)        
            failed += 1

    print('Total tests:', count, 'Tests passed:', passed)
    print('-------------------------------------------')

    score = [(1,0), (3,4), (7,8), (10,10), (11, 12)
	]

    for (p,s) in score:
        if passed <= p:
            print('Passed:', passed, 'Resulting Grade:', s, 'out of 12')
            break
    return
    


#########################################################################
# testing for randchain()
# check base case: n = 0
#     - check for structure (should be None)
# check case n = 1
#     - check structure and content of the node chain
# check case n = 5
#     - check structure and content of the node chain

def test_randchain_empty():
    """ Test randchain()
        Create an empty chain.
        Check that the result is None.
    """
    n = 0
    stuff = []
    result = A8.randchain(n, stuff)

    assert result is None, "randchain did not create an empty chain with n = 0"


def test_randchain_singleton():
    """ Test randchain()
        Create a chain of length 1.
        Check that the result is not None.
    """
    n = 1
    stuff = [1]
    result = A8.randchain(n, stuff)

    assert result is not None, "randchain created empty chain with n = 1"


def test_randchain_singleton_content():
    """ Test randchain()
        Create a chain of length 1.
        Check that the result contains the correct data value.
    """
    n = 1
    stuff = [1]
    chain = A8.randchain(n, stuff)

    result = chain.data
    expected = 1
    assert result == expected, "randchain did not choose a value from stuff"


def test_randchain_singleton_structure():
    """ Test randchain()
        Create a chain of length 1.
        Check that the result node has next == None.
    """
    n = 1
    stuff = [1]
    chain = A8.randchain(n, stuff)

    result = chain.next
    expected = None
    assert result == expected, "randchain did not create a well-formed chain with n = 1"


def test_randchain_multiple():
    """ Test randchain()
        Create a chain of length > 1
        Check that the result is not None.
    """
    n = 5
    stuff = list(range(100))
    result = A8.randchain(n, stuff)

    assert result is not None, "randchain created empty chain with n = 5"


def test_randchain_multiple_structure():
    """ Test randchain()
        Create a chain of length > 1
        Check that the result is a node chain of exactly the required length
    """
    n = 5
    stuff = list(range(10*n))
    result = A8.randchain(n, stuff)

    # try to take exactly n steps along the result
    walker = result
    for i in range(n):
        assert walker is not None, "randchain created a chain that terminated at index {}".format(i)
        walker = walker.next

    assert walker is None, "randchain created a chain that did not terminate properly at index {}".format(i)


def test_randchain_multiple_content():
    """ Test randchain()
        Create a chain of length > 1
        Check that the result is a node chain has values chosen from the stuff.
        A weak test, but better than nothing?
    """
    n = 5
    stuff = list(range(10*n))
    result = A8.randchain(n, stuff)

    walker = result
    for i in range(n):
        assert walker.data in stuff, "randchain data value {} not in stuff".format(walker.data)
        walker = walker.next

#########################################################################
# testing for to_string()
# check base case: n = 0
#     - check for correct output
# check case n = 1
#     - check for correct output
# check case n = 2
#     - check for correct output
# check case n = 3
#     - check for correct output

def test_to_string_empty():
    """ Test to_string()
        Create an empty node chain.
        Check correct output
    """
    chain = None
    result = A8.to_string(chain)
    expected = "EMPTY"

    assert result == expected, "to_string returned '{}'; expected '{}' for emtpy chain".format(result, expected)


def test_to_string_singleton():
    """ Test to_string()
        Create a node chain of length 1.
        Check correct output
    """
    data = 1
    chain = N.Node(data)
    result = A8.to_string(chain)
    expected = "{}".format(data)

    assert result == expected, "to_string returned '{}'; expected '{}' for singleton chain".format(result, expected)


def test_to_string_two():
    """ Test to_string()
        Create a node chain of length 2.
        Check correct output
    """
    data1 = 1
    data2 = 2
    chain = N.Node(data1, N.Node(data2))
    result = A8.to_string(chain)
    expected = "{} -> {}".format(data1, data2)

    assert result == expected, "to_string returned '{}'; expected '{}' for chain length 2".format(result, expected)


def test_to_string_three():
    """ Test to_string()
        Create a node chain of length 3.
        Check correct output
    """
    data1 = 1
    data2 = 2
    data3 = 'c'
    chain = N.Node(data1, N.Node(data2, N.Node(data3)))
    result = A8.to_string(chain)
    expected = "{} -> {} -> {}".format(data1, data2, data3)

    assert result == expected, "to_string returned '{}'; expected '{}' for chain length 3".format(result, expected)



# a list of references to the functions defined above
all_of_em = [
     test_to_string_empty,
     test_to_string_singleton,
     test_to_string_two,
     test_to_string_three,
     test_randchain_empty,
     test_randchain_singleton,
     test_randchain_singleton_content,
     test_randchain_singleton_structure,
     test_randchain_multiple,
     test_randchain_multiple_structure,
     test_randchain_multiple_content
    ]


runemall()

