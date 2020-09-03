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
#     scoring script for A8Q2
#     student version
#
#     Run this script to see how many of your functions work!
#     

import node as N
import A8Q2 as A8

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

    score = [(2,0), (5, 6), (14, 9), (21, 12), (29,15), (30, 16)
	]

    for (p,s) in score:
        if passed <= p:
            print('Passed:', passed, 'Resulting Grade:', s, 'out of 16')
            break
    return
    



###################
# test insert_node:
# base case: empty chain
# case: chain length 1:
#   - less than
#   - equal to
#   - greater than
# case: chain length 2
#   - insert first
#   - insert between
#   - insert last


def test_insert_node_empty_structure():
    """ Test insert_node()
        base case: insert into empty chain
        check structure
    """
    chain = None
    node = N.Node(1)

    result = A8.insert_node(node, chain)

    assert result is not None, "insert_chain returned empty chain given a node and empty chain"
    assert result.next is None, "insert_chain returned badly formed chain given a node and empty chain"


def test_insert_node_empty_content():
    """ Test insert_node()
        base case: insert into empty chain
        check content
    """
    chain = None
    expected = 1
    node = N.Node(expected)

    result = A8.insert_node(node, chain)

    assert result.data == expected, "insert_chain returned extraneous data in chain given a node and empty chain"


def test_insert_node_singleton_structure_1():
    """ Test insert_node()
        insert node into chain of length 1
            - new data smaller than first data
        check structure
    """
    chain = N.Node(1)
    node = N.Node(0)

    result = A8.insert_node(node, chain)

    assert result is not None, "insert_node returned empty chain given a node and singleton chain"
    assert result.next is not None, "insert_node returned short chain given a node and singleton chain"
    assert result.next.next is None, "insert_node returned badly formed chain given a node and singleton chain"


def test_insert_node_singleton_structure_2():
    """ Test insert_node()
        insert node into chain of length 1
            - new data equal to first data
        check structure
    """
    chain = N.Node(1)
    node = N.Node(1)

    result = A8.insert_node(node, chain)

    assert result is not None, "insert_node returned empty chain given a node and singleton chain"
    assert result.next is not None, "insert_node returned short chain given a node and singleton chain"
    assert result.next.next is None, "insert_node returned badly formed chain given a node and singleton chain"


def test_insert_node_singleton_structure_3():
    """ Test insert_node()
        insert node into chain of length 1
            - new data greater than first data
        check structure
    """
    chain = N.Node(1)
    node = N.Node(2)

    result = A8.insert_node(node, chain)

    assert result is not None, "insert_node returned empty chain given a node and singleton chain"
    assert result.next is not None, "insert_node returned short chain given a node and singleton chain"
    assert result.next.next is None, "insert_node returned badly formed chain given a node and singleton chain"


def test_insert_node_singleton_content_1():
    """ Test insert_node()
        insert node into chain of length 1
            - new data smaller than first data
        check content
    """
    first = 0
    second = 1
    chain = N.Node(second)
    node = N.Node(first)

    result = A8.insert_node(node, chain)

    assert result.data == first, "insert_node returned incorrect data value first given a node and singleton chain"
    assert result.next.data == second, "insert_node returned incorrect data value second given a node and singleton chain"


def test_insert_node_singleton_content_2():
    """ Test insert_node()
        insert node into chain of length 1
            - new data equal to first data
        check content
    """
    first = 0
    second = first
    chain = N.Node(second)
    node = N.Node(first)

    result = A8.insert_node(node, chain)

    assert result.data == first, "insert_node returned incorrect data value first given a node and singleton chain"
    assert result.next.data == second, "insert_node returned incorrect data value second given a node and singleton chain"


def test_insert_node_singleton_content_3():
    """ Test insert_node()
        insert node into chain of length 1
            - new data greater than first data
        check content
    """
    first = 0
    second = 1
    chain = N.Node(first)
    node = N.Node(second)

    result = A8.insert_node(node, chain)

    assert result.data == first, "insert_node returned incorrect data value first given a node and singleton chain"
    assert result.next.data == second, "insert_node returned incorrect data value second given a node and singleton chain"


def test_insert_node_multiple_structure_1():
    """ Test insert_node()
        insert node into chain of length 2
            - new data smaller than first data
        check structure
    """
    chain = N.Node(1, N.Node(3))
    node = N.Node(0)

    result = A8.insert_node(node, chain)

    assert result is not None, "insert_node returned empty chain given a node and chain length 2 (insert at start)"
    assert result.next is not None, "insert_node returned short chain given a node and chain length 2 (insert at start)"
    assert result.next.next is not None, "insert_node returned short chain given a node and chain length 2 (insert at start)"
    assert result.next.next.next is None, "insert_node returned badly formed chain given a node and chain length 2 (insert at start)"


def test_insert_node_multiple_structure_2():
    """ Test insert_node()
        insert node into chain of length 2
            - new data between first and second 
        check structure
    """
    chain = N.Node(1, N.Node(3))
    node = N.Node(2)

    result = A8.insert_node(node, chain)

    assert result is not None, "insert_node returned empty chain given a node and chain length 2 (insert between)"
    assert result.next is not None, "insert_node returned short chain given a node and chain length 2 (insert between)"
    assert result.next.next is not None, "insert_node returned short chain given a node and chain length 2 (insert between)"
    assert result.next.next.next is None, "insert_node returned badly formed chain given a node and chain length 2 (insert between)"


def test_insert_node_multiple_structure_3():
    """ Test insert_node()
        insert node into chain of length 2
            - new data greater than second data
        check structure
    """
    chain = N.Node(1, N.Node(3))
    node = N.Node(4)

    result = A8.insert_node(node, chain)

    assert result is not None, "insert_node returned empty chain given a node and chain length 2 (insert at end)"
    assert result.next is not None, "insert_node returned short chain given a node and chain length 2 (insert at end)"
    assert result.next.next is not None, "insert_node returned short chain given a node and chain length 2 (insert at end)"
    assert result.next.next.next is None, "insert_node returned badly formed chain given a node and chain length 2 (insert at end)"


def test_insert_node_multiple_content_1():
    """ Test insert_node()
        insert node into chain of length 2
            - new data smaller than first data
        check content
    """
    first = 0
    second = 1
    third = 3
    chain = N.Node(second, N.Node(third))
    node = N.Node(first)

    result = A8.insert_node(node, chain)

    assert result.data == first, "insert_node returned incorrect data value first given a node and chain length 2 (insert at start)"
    assert result.next.data == second, "insert_node returned incorrect data value second given a node and chain length 2 (insert at start)"
    assert result.next.next.data == third, "insert_node returned incorrect data value second given a node and chain length 2 (insert at start)"


def test_insert_node_multiple_content_2():
    """ Test insert_node()
        insert node into chain of length 2
            - new data greater than first data, smaller than second
        check content
    """
    first = 0
    second = 1
    third = 3
    chain = N.Node(first, N.Node(third))
    node = N.Node(second)

    result = A8.insert_node(node, chain)

    assert result.data == first, "insert_node returned incorrect data value first given a node and chain length 2 (insert at mid)"
    assert result.next.data == second, "insert_node returned incorrect data value second given a node and chain length 2 (insert at middle)"
    assert result.next.next.data == third, "insert_node returned incorrect data value second given a node and chain length 2 (insert at middle)"


def test_insert_node_multiple_content_3():
    """ Test insert_node()
        insert node into chain of length 2
            - new data greater than second data
        check content
    """
    first = 0
    second = 1
    third = 3
    chain = N.Node(first, N.Node(second))
    node = N.Node(third)

    result = A8.insert_node(node, chain)

    assert result.data == first, "insert_node returned incorrect data value first given a node and chain length 2 (insert at end)"
    assert result.next.data == second, "insert_node returned incorrect data value second given a node and chain length 2 (insert at end)"
    assert result.next.next.data == third, "insert_node returned incorrect data value second given a node and chain length 2 (insert at end)"


#########################################################################################
# test sort_chain:
# base case: empty chain
#   - check structure
# case: chain length 1:
#   - check structure and content
# case: chain length 2
#   - in order already
#       - check structure and content
#   - not in order yet
#       - check structure and content
# case: longer chains
#   - in order already
#       - check structure and content
#   - in reverse order
#       - check structure and content
#   - in randomish order
#       - check structure and content
# case: longer chains
#   - check that nodes are re-ordered, not d created new
#   - check that data values are in the nodes they started in


def test_sort_chain_empty():
    """ Test sort_chain()
        base case: sort an empty chain
    """
    chain = None
    result = A8.sort_chain(chain)

    assert result is None, "sort_chain returned non-empty chain given empty input"


def test_sort_chain_singleton_structure():
    """ Test sort_chain()
        sort a chain length 1
        check structure
    """
    chain = N.Node(1)
    result = A8.sort_chain(chain)

    assert result is not None, "sort_chain returned empty chain given singleton input"
    assert result.next is None, "sort_chain returned extended chain given singleton input"


def test_sort_chain_singleton_content():
    """ Test sort_chain()
        sort a chain length 1
        check content    
    """
    expected = 1
    chain = N.Node(expected)
    result = A8.sort_chain(chain)

    assert result.data == 1, "sort_chain returned extraneous data given singleton input; expected {} found {}".format(expected, result.data)


def test_sort_chain_two_structure():
    """ Test sort_chain()
        sort a chain length 2 - already in order
        check structure
    """
    chain = N.Node(1, N.Node(2))
    result = A8.sort_chain(chain)

    assert result is not None, "sort_chain returned empty chain given input chain size 2 already in order"
    assert result.next is not None, "sort_chain returned singleton chain given input chain size 2 already in order"
    assert result.next.next is None, "sort_chain returned extended chain given input chain size 2 already in order"


def test_sort_chain_two_content():
    """ Test sort_chain()
        sort a chain length 2 - already in order
        check content    
    """
    chain = N.Node(1, N.Node(2))
    result = A8.sort_chain(chain)

    assert result.data <= result.next.data, "sort_chain returned chain out of order given input chain size 2 already in order"


def test_sort_chain_two_structure_2():
    """ Test sort_chain()
        sort a chain length 2 - reverse order
        check structure    
    """
    chain = N.Node(3, N.Node(2))
    result = A8.sort_chain(chain)

    assert result is not None, "sort_chain returned empty chain given input chain size 2 in reverse order"
    assert result.next is not None, "sort_chain returned singleton chain given input chain size 2 in reverse order"
    assert result.next.next is None, "sort_chain returned extended chain given input chain size 2 in reverse order"


def test_sort_chain_two_content_2():
    """ Test sort_chain()
        sort a chain length 2 - reverse order
        check content 
    """
    chain = N.Node(3, N.Node(2))
    result = A8.sort_chain(chain)

    assert result.data <= result.next.data, "sort_chain returned chain out of order given input chain size 2 in reverse order"


def test_sort_chain_two_structure_3():
    """ Test sort_chain()
        sort a chain length 2 - all same
        check structure 
    """
    chain = N.Node(2, N.Node(2))
    result = A8.sort_chain(chain)

    assert result is not None, "sort_chain returned empty chain given input chain size 2 with dupicates"
    assert result.next is not None, "sort_chain returned singleton chain given input chain size 2 with dupicates"
    assert result.next.next is None, "sort_chain returned extended chain given input chain size 2 with dupicates"


def test_sort_chain_two_content_3():
    """ Test sort_chain()
        sort a chain length 2 - all same
        check content 
    """
    chain = N.Node(2, N.Node(2))
    result = A8.sort_chain(chain)

    assert result.data <= result.next.data, "sort_chain returned chain out of order given input chain size 2 with dupicates"


def test_sort_chain_multiple_structure_increasing():
    """ Test sort_chain()
        sort larger chain already in order
        check structure
    """
    n = 11
    data = range(n)
    chain = None
    for item in data:
        chain = N.Node(n-item, chain)

    result = A8.sort_chain(chain)

    walker = result
    for i in range(n):
        assert walker is not None, "sort_chain returned chain of length {} given chain with values increasing".format(i)
        walker = walker.next

    assert walker is None, "sort_chain returned chain longer than length {} given chain with values increasing".format(n)


def test_sort_chain_multiple_structure_decreasing():
    """ Test sort_chain()
        sort larger chain decreasing order
        check structure
    """
    n = 14
    data = range(n)
    chain = None
    for item in data:
        chain = N.Node(item, chain)

    result = A8.sort_chain(chain)

    walker = result
    for i in range(n):
        assert walker is not None, "sort_chain returned chain of length {} given chain with values decreasing".format(i)
        walker = walker.next

    assert walker is None, "sort_chain returned chain longer than length {} given chain with values decreasing".format(n)


def test_sort_chain_multiple_structure_random():
    """ Test sort_chain()
        sort larger chain random order
        check structure
    """
    data = [-10, 42, 8, 64, -6, 76, 48, 8, -30, 1, 11, 92, 37, 4]
    chain = None
    for item in data:
        chain = N.Node(item, chain)

    result = A8.sort_chain(chain)

    walker = result
    for i in range(len(data)):
        assert walker is not None, "sort_chain returned chain of length {} given chain with randomish values".format(i)
        walker = walker.next

    assert walker is None, "sort_chain returned chain longer than length {} given chain with randomish values".format(len(data))


def test_sort_chain_multiple_content_increasing():
    """ Test sort_chain()
        sort larger chain already in order
        check content
    """
    n = 11
    data = range(n)
    chain = None
    for item in data:
        chain = N.Node(n-item-1, chain)

    result = A8.sort_chain(chain)

    walker = result
    prev = None
    seen = [False]*n
    for i in range(n):
        assert walker.data in data, "sort_chain created extraneous data {} given chain with values increasing".format(walker.data)
        seen[walker.data] = True
        if prev is not None:
            assert prev.data <= walker.data, "sort_chain placed {} before {} given chain with values increasing".format(prev.data, walker.data)
        prev = walker
        walker = walker.next

    for i,b in enumerate(seen):
        assert b, "sort_chain omitted data value {} from returned chain given chain with values increasing".format(i)


def test_sort_chain_multiple_content_decreasing():
    """ Test sort_chain()
        sort larger chain decreasing order
        check content
    """
    n = 17
    data = range(n)
    chain = None
    for item in data:
        chain = N.Node(item, chain)

    result = A8.sort_chain(chain)

    walker = result
    prev = None
    seen = [False]*n
    for i in range(n):
        assert walker.data in data, "sort_chain created extraneous data {} given chain with values decreasing".format(walker.data)
        seen[walker.data] = True
        if prev is not None:
            assert prev.data <= walker.data, "sort_chain placed {} before {} given chain with values decreasing".format(prev.data, walker.data)
        prev = walker
        walker = walker.next

    for i,b in enumerate(seen):
        assert b, "sort_chain omitted data value {} from returned chain given chain with values decreasing".format(i)


def test_sort_chain_multiple_content_random():
    """ Test sort_chain()
        sort larger chain random order
        check content
    """
    data = [-10, 42, 8, 64, -6, 76, 48, 8, -30, 1, 11, 92, 37, 4]
    chain = None
    for item in data:
        chain = N.Node(item, chain)

    result = A8.sort_chain(chain)

    walker = result
    prev = None
    seen = {}
    for v in data:
        seen[v] = False
    for i in range(len(data)):
        assert walker.data in data, "sort_chain created extraneous data {} given chain with with randomish values".format(walker.data)
        seen[walker.data] = True
        if prev is not None:
            assert prev.data <= walker.data, "sort_chain placed {} before {} given chain with with randomish values".format(prev.data, walker.data)
        prev = walker
        walker = walker.next

    for k in seen:
        assert seen[k], "sort_chain omitted data value {} from returned chain given chain with with randomish values".format(k)


def test_sort_chain_multiple_reuse():
    """ Test sort_chain()
        Check whether the sorting method reuses the same nodes as the original
        This test will fail if the sorting method creates new nodes, or if the 
        data values are copied to other nodes in the chain.
    """
    data = [-10, 42, 8, 64, -6, 76, 48, 8, -30, 1, 11, 92, 37, 4]
    chain = None
    for item in data:
        chain = N.Node(item, chain)

    id_record = {}
    walker = chain
    while walker is not None:
        id_record[id(walker)] = walker.data
        walker = walker.next

    result = A8.sort_chain(chain)

    walker = result
    while walker is not None:
        assert id(walker) in id_record, "sort_chain created new node"
        assert id_record[id(walker)] == walker.data, "sort_chain moved data value {} to new node".format(walker.data)
        walker = walker.next


# a list of references to the functions defined above
all_of_em = [
     test_insert_node_empty_structure,
     test_insert_node_empty_content,
     test_insert_node_singleton_structure_1,
     test_insert_node_singleton_structure_2,
     test_insert_node_singleton_structure_3,
     test_insert_node_singleton_content_1,
     test_insert_node_singleton_content_2,
     test_insert_node_singleton_content_3,
     test_insert_node_multiple_structure_1,
     test_insert_node_multiple_structure_2,
     test_insert_node_multiple_structure_3,
     test_insert_node_multiple_content_1,
     test_insert_node_multiple_content_2,
     test_insert_node_multiple_content_3,
     test_sort_chain_empty,
     test_sort_chain_singleton_structure,
     test_sort_chain_singleton_content,
     test_sort_chain_two_structure,
     test_sort_chain_two_content,
     test_sort_chain_two_structure_2,
     test_sort_chain_two_content_2,
     test_sort_chain_two_structure_3,
     test_sort_chain_two_content_3,
     test_sort_chain_multiple_structure_increasing,
     test_sort_chain_multiple_structure_decreasing,
     test_sort_chain_multiple_structure_random,
     test_sort_chain_multiple_content_increasing,
     test_sort_chain_multiple_content_decreasing,
     test_sort_chain_multiple_content_random,
     test_sort_chain_multiple_reuse
    ]


runemall()

