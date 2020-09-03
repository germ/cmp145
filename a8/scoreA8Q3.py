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
#     scoring script for A8Q3
#     student version
#
#     Run this script to see how many of your functions work!
#     

import node as N
import A8Q3 as A8

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

    score = [(4,0), (21, 3), (35,5), (42,6), (49,7), (50, 8)
	]

    for (p,s) in score:
        if passed <= p:
            print('Passed:', passed, 'Resulting Grade:', s, 'out of 8')
            break
    return
    


#########################################################################
# testing for split_chain()
# check base case: n = 0
#     - check for correct output
# check case n = 1
#     - check for correct output
# check case n = 2
#     - check for correct output
# check case n = 3
#     - check for correct output

def test_split_chain_empty():
    """ Test split_chain()
    """
    chain = None
    pivot = 0

    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    assert result_l is None and result_e is None and result_g is None, "split_chain did not return empty chains given empty chain"


def test_split_chain_singleton_structure():
    """ Test split_chain()
    """
    chain = N.Node(1)
    pivot = 0

    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    assert result_l is None, "split_chain did not return empty lesser chain on singleton chain"
    assert result_e is None, "split_chain did not return empty equal chain on singleton chain"
    assert result_g is not None, "split_chain returned empty greater chain on singleton chain"
    assert result_g.next is None, "split_chain returned badly formed greater chain on singleton chain"


def test_split_chain_singleton_structure():
    """ Test split_chain()
    """
    chain = N.Node(1)
    pivot = 1

    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    assert result_l is None, "split_chain did not return empty lesser chain on singleton chain"
    assert result_g is None, "split_chain did not return empty greater chain on singleton chain"
    assert result_e is not None, "split_chain returned empty equal chain on singleton chain"
    assert result_e.next is None, "split_chain returned badly formed equal chain on singleton chain"


def test_split_chain_singleton_structure():
    """ Test split_chain()
    """
    chain = N.Node(1)
    pivot = 2

    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    assert result_g is None, "split_chain did not return empty greater chain on singleton chain"
    assert result_e is None, "split_chain did not return empty equal chain on singleton chain"
    assert result_l is not None, "split_chain returned empty lesser chain on singleton chain"
    assert result_l.next is None, "split_chain returned badly formed lesser chain on singleton chain"


def test_split_chain_singleton_content_1():
    """ Test split_chain()
    """
    expected = 1
    chain = N.Node(expected)
    pivot = 0

    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    assert result_g.data == expected, "split_chain returned extraneous data {} in greater chain on singleton chain".format(result.data)


def test_split_chain_singleton_content_2():
    """ Test split_chain()
    """
    expected = 1
    chain = N.Node(expected)
    pivot = 1

    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    assert result_e.data == expected, "split_chain returned extraneous data {} in equal chain on singleton chain".format(result.data)

def test_split_chain_singleton_content_3():
    """ Test split_chain()
    """
    expected = 1
    chain = N.Node(expected)
    pivot = 2

    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    assert result_l.data == expected, "split_chain returned extraneous data {} in lesser chain on singleton chain".format(result.data)


def test_split_chain_two_structure_1():
    """ Test split_chain()
    """
    data1 = 1
    data2 = 3
    chain = N.Node(data1, N.Node(data2))
    pivot = 0
    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    assert result_l is None, "split_chain did not return empty lesser chain given chain length 2"
    assert result_e is None, "split_chain did not return empty equal chain given chain length 2"
    assert result_g is not None, "split_chain returned empty greater chain given chain length 2"
    assert result_g.next is not None, "split_chain returned greater chain too short given chain length 2"
    assert result_g.next.next is  None, "split_chain returned greater chain too long given chain length 2"


def test_split_chain_two_structure_2():
    """ Test split_chain()
    """
    data1 = 1
    data2 = 3
    chain = N.Node(data1, N.Node(data2))
    pivot = 1
    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    assert result_l is None, "split_chain did not return empty lesser chain given chain length 2"
    assert result_e is not None, "split_chain returned empty equal chain given chain length 2"
    assert result_e.next is None, "split_chain returned badly formed equal chain given chain length 2"
    assert result_g is not None, "split_chain returned empty greater chain given chain length 2"
    assert result_g.next is None, "split_chain returned badly formed greater chain given chain length 2"

def test_split_chain_two_structure_3():
    """ Test split_chain()
    """
    data1 = 1
    data2 = 3
    chain = N.Node(data1, N.Node(data2))
    pivot = 2
    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    assert result_e is None, "split_chain did not return empty equal chain given chain length 2"
    assert result_l is not None, "split_chain returned empty lesser chain given chain length 2"
    assert result_l.next is None, "split_chain returned badly formed lesser chain given chain length 2"
    assert result_g is not None, "split_chain returned empty greater chain given chain length 2"
    assert result_g.next is None, "split_chain returned badly formed greater chain given chain length 2"

def test_split_chain_two_structure_3():
    """ Test split_chain()
    """
    data1 = 1
    data2 = 3
    chain = N.Node(data1, N.Node(data2))
    pivot = 3
    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    assert result_g is None, "split_chain did not return empty equal chain given chain length 2"
    assert result_l is not None, "split_chain returned empty lesser chain given chain length 2"
    assert result_l.next is None, "split_chain returned badly formed lesser chain given chain length 2"
    assert result_e is not None, "split_chain returned empty equal chain given chain length 2"
    assert result_e.next is None, "split_chain returned badly formed equal chain given chain length 2"

def test_split_chain_two_structure_3():
    """ Test split_chain()
    """
    data1 = 1
    data2 = 3
    chain = N.Node(data1, N.Node(data2))
    pivot = 4
    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    assert result_g is None, "split_chain did not return empty greater chain given chain length 2"
    assert result_e is None, "split_chain did not return empty equal chain given chain length 2"
    assert result_l is not None, "split_chain returned empty lesser chain given chain length 2"
    assert result_l.next is not None, "split_chain returned lesser chain too short given chain length 2"
    assert result_l.next.next is  None, "split_chain returned lesser chain too long given chain length 2"


def test_split_chain_two_content_1():
    """ Test split_chain()
    """
    data1 = 1
    data2 = 3
    chain = N.Node(data1, N.Node(data2))
    pivot = 0
    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    check_1 = result_g.data == 1 or result_g.next.data == 1
    check_3 = result_g.data == 3 or result_g.next.data == 3
    check_diff = result_g.data != result_g.next.data

    assert check_1 and check_3 and check_diff, "split_chain did not preserve the data values given chain length 2, expected {} and {}, found {} and {}".format(data1, data2, result_g.data, result_g.next.data)


def test_split_chain_two_content_2():
    """ Test split_chain()
    """
    data1 = 1
    data2 = 3
    chain = N.Node(data1, N.Node(data2))
    pivot = 1
    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    check_1 = result_e.data == 1
    check_3 = result_g.data == 3

    assert check_1 and check_3, "split_chain did not preserve the data values given chain length 2, expected {} and {}, found {} and {}".format(
        data1, data2, result_e.data, result_g.data)

def test_split_chain_two_content_3():
    """ Test split_chain()
    """
    data1 = 1
    data2 = 3
    chain = N.Node(data1, N.Node(data2))
    pivot = 2
    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    check_1 = result_l.data == 1
    check_3 = result_g.data == 3

    assert check_1 and check_3, "split_chain did not preserve the data values given chain length 2, expected {} and {}, found {} and {}".format(
        data1, data2, result_e.data, result_g.data)


def test_split_chain_two_content_4():
    """ Test split_chain()
    """
    data1 = 1
    data2 = 3
    chain = N.Node(data1, N.Node(data2))
    pivot = 3
    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    check_1 = result_l.data == 1
    check_3 = result_e.data == 3

    assert check_1 and check_3, "split_chain did not preserve the data values given chain length 2, expected {} and {}, found {} and {}".format(
        data1, data2, result_e.data, result_g.data)

def test_split_chain_two_content_5():
    """ Test split_chain()
    """
    data1 = 1
    data2 = 3
    chain = N.Node(data1, N.Node(data2))
    pivot = 4
    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    check_1 = result_l.data == 1 or result_l.next.data == 1
    check_3 = result_l.data == 3 or result_l.next.data == 3
    check_diff = result_l.data != result_l.next.data

    assert check_1 and check_3 and check_diff, "split_chain did not preserve the data values given chain length 2, expected {} and {}, found {} and {}".format(data1, data2, result_g.data, result_g.next.data)



def test_split_chain_multiple_structure_1():
    """ Test split_chain()
    """
    data = [1, 3, 1, 4, 3, 5, 3, 1, 4]
    n = len(data)
    chain = None
    for item in data:
        chain = N.Node(item, chain)

    # all values go to greater chain
    pivot = 0
    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    assert result_l is None, "split_chain returned non-empty lesser chain given pivot smaller than all data values"
    assert result_e is None, "split_chain returned non-empty equal chain given pivot smaller than all data values"
    walker = result_g
    for i in range(n):
        assert walker is not None, "split_chain returned short greater chain for length {}, terminated at index {}".format(2*n, i)
        walker = walker.next

    assert walker is None, "split_chain returned greater chain longer than length {}".format(n)


def test_split_chain_multiple_structure_2():
    """ Test split_chain()
    """
    data = [1, 3, 1, 4, 3, 5, 3, 1, 4]
    n = len(data)
    chain = None
    for item in data:
        chain = N.Node(item, chain)

    # all values go to lesser chain
    pivot = 10
    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    assert result_g is None, "split_chain returned non-empty greater chain given pivot smaller than all data values"
    assert result_e is None, "split_chain returned non-empty equal chain given pivot smaller than all data values"
    walker = result_l
    for i in range(n):
        assert walker is not None, "split_chain returned short lesser chain for length {}, terminated at index {}".format(2*n, i)
        walker = walker.next

    assert walker is None, "split_chain returned lesser chain longer than length {}".format(n)

def test_split_chain_multiple_structure_3():
    """ Test split_chain()
    """
    data = [1]*7
    n = len(data)
    chain = None
    for item in data:
        chain = N.Node(item, chain)

    # all values go to equal chain
    pivot = 1
    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    assert result_g is None, "split_chain returned non-empty greater chain given pivot smaller than all data values"
    assert result_l is None, "split_chain returned non-empty lesser chain given pivot smaller than all data values"
    walker = result_e
    for i in range(n):
        assert walker is not None, "split_chain returned short equal chain for length {}, terminated at index {}".format(2*n, i)
        walker = walker.next

    assert walker is None, "split_chain returned equal chain longer than length {}".format(n)

def test_split_chain_multiple_structure_4():
    """ Test split_chain()
    """
    data = [1, 3, 1, 2, 4, 3, 5, 3, 1, 4]
    n = len(data)
    chain = None
    for item in data:
        chain = N.Node(item, chain)

    # send values to all chains
    pivot = 3
    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    # check the lesser chain
    n_less = sum([1 for v in data if v < pivot])
    walker = result_l
    for i in range(n_less):
        assert walker is not None, "split_chain returned short lesser chain for length {}, terminated at index {}".format(n_less, i)
        walker = walker.next

    assert walker is None, "split_chain returned lesser chain longer than length {}".format(n)

    # check the equal chain
    n_equal = sum([1 for v in data if v == pivot])
    walker = result_e
    for i in range(n_equal):
        assert walker is not None, "split_chain returned short equal chain for length {}, terminated at index {}".format(n_equal, i)
        walker = walker.next

    assert walker is None, "split_chain returned equal chain longer than length {}".format(n)

    # check the greater chain
    n_greater = sum([1 for v in data if v > pivot])
    walker = result_g
    for i in range(n_greater):
        assert walker is not None, "split_chain returned short lesser chain for length {}, terminated at index {}".format(n_greater, i)
        walker = walker.next

    assert walker is None, "split_chain returned lesser chain longer than length {}".format(n)


def test_split_chain_multiple_content_1():
    """ Test split_chain()
    """
    data = [1, 3, 1, 4, 3, 5, 3, 1, 4]
    n = len(data)
    chain = None
    for item in data:
        chain = N.Node(item, chain)

    # all values go to greater chain
    pivot = 0
    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    seen = {}
    for v in data:
        seen[v] = 0

    walker = result_g
    while walker is not None:
        assert walker.data in data, "split_chain extraneous data value in greater chain for length {}".format(n)
        seen[walker.data] += 1
        walker = walker.next

    for v in data:
        expected = sum([1 for d in data if v == d])
        assert seen[v] == expected, "split_chain greater chain contained incorrect number of data value {}: expected {} found {}".format(v, expected, seen[v])

def test_split_chain_multiple_content_2():
    """ Test split_chain()
    """
    data = [1, 3, 1, 4, 3, 5, 3, 1, 4]
    n = len(data)
    chain = None
    for item in data:
        chain = N.Node(item, chain)

    # all values go to lesser chain
    pivot = 10
    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    seen = {}
    for v in data:
        seen[v] = 0

    walker = result_l
    while walker is not None:
        assert walker.data in data, "split_chain extraneous data value in lesser chain for length {}".format(n)
        seen[walker.data] += 1
        walker = walker.next

    for v in data:
        expected = sum([1 for d in data if v == d])
        assert seen[v] == expected, "split_chain lesser chain contained incorrect number of data value {}: expected {} found {}".format(v, expected, seen[v])

def test_split_chain_multiple_content_3():
    """ Test split_chain()
    """
    data = [1]*7
    n = len(data)
    chain = None
    for item in data:
        chain = N.Node(item, chain)

    # all values go to equal chain
    pivot = 1
    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    seen = {}
    for v in data:
        seen[v] = 0

    walker = result_e
    while walker is not None:
        assert walker.data in data, "split_chain extraneous data value in equal chain for length {}".format(n)
        seen[walker.data] += 1
        walker = walker.next

    for v in data:
        expected = sum([1 for d in data if v == d])
        assert seen[v] == expected, "split_chain equal chain contained incorrect number of data value {}: expected {} found {}".format(v, expected, seen[v])


def test_split_chain_multiple_content_4():
    """ Test split_chain()
    """
    data = [1, 3, 1, 4, 3, 5, 3, 1, 4]
    n = len(data)
    chain = None
    for item in data:
        chain = N.Node(item, chain)

    # values go to all chains
    pivot = 3
    result_l, result_e, result_g = A8.split_chain(pivot, chain)

    seen = {}
    for v in data:
        seen[v] = 0

    walker = result_l
    while walker is not None:
        assert walker.data < pivot, "split_chain incorrectly place data value in lesser chain for length {}: found {} for pivot {}".format(n, walker.data, pivot)
        seen[walker.data] += 1
        walker = walker.next

    walker = result_e
    while walker is not None:
        assert walker.data == pivot, "split_chain incorrectly place data value in equal chain for length {}: found {} for pivot {}".format(n, walker.data, pivot)
        seen[walker.data] += 1
        walker = walker.next

    walker = result_g
    while walker is not None:
        assert walker.data > pivot, "split_chain incorrectly place data value in greater chain for length {}: found {} for pivot {}".format(n, walker.data, pivot)
        seen[walker.data] += 1
        walker = walker.next

    for v in data:
        expected = sum([1 for d in data if v == d])
        assert seen[v] == expected, "split_chain returned incorrect number of data value {}: expected {} found {}".format(v, expected, seen[v])


#########################################################################
# testing for extend_chain()


def test_extend_chain_empty():
    """ Test extend_chain()
    """
    chain1 = None
    chain2 = None

    result = A8.extend_chain(chain1, chain2)
    assert result is None, "extend_chain did not return empty chain given two empty chains"

def test_extend_chain_singleton_structure_1():
    """ Test extend_chain()
    """
    chain1 = N.Node(1)
    chain2 = None

    result = A8.extend_chain(chain1, chain2)
    assert result is not None, "extend_chain returned empty chain given one non-empty chain"
    assert result.next is None, "extend_chain returned chain longer than 1 node given one non-empty chain"

def test_extend_chain_singleton_structure_2():
    """ Test extend_chain()
    """
    chain2 = N.Node(1)
    chain1 = None

    result = A8.extend_chain(chain1, chain2)
    assert result is not None, "extend_chain returned empty chain given one non-empty chain"
    assert result.next is None, "extend_chain returned chain longer than 1 node given one non-empty chain"

def test_extend_chain_singleton_structure_3():
    """ Test extend_chain()
    """
    chain2 = N.Node(1)
    chain1 = N.Node(2)

    result = A8.extend_chain(chain1, chain2)
    assert result is not None, "extend_chain returned empty chain given two non-empty chains"
    assert result.next is not None, "extend_chain returned chain of 1 node given two singleton chains"
    assert result.next.next is None, "extend_chain returned chain longer than 1 node given two non-empty chains"

def test_extend_chain_multiple_structure_3():
    """ Test extend_chain()
    """
    chain1 = N.Node(1, N.Node(3))
    chain2 = N.Node(2, N.Node(4))

    result = A8.extend_chain(chain1, chain2)

    walker = result
    for i in range(4):
        assert walker is not None, 'extend_chain return shortened chain, given two chains of length 2, terminated at index {}'.format(i)
        walker = walker.next
        
    assert walker is None, 'extend_chain returned chain too long given two chains of length 2'


def test_extend_chain_singleton_content_1():
    """ Test extend_chain()
    """
    expected = 1
    chain1 = N.Node(expected)
    chain2 = None

    result = A8.extend_chain(chain1, chain2)
    assert result.data == expected, "extend_chain returned unexpected data value, found {} expected {}".format(result.data, expected)

def test_extend_chain_singleton_content_2():
    """ Test extend_chain()
    """
    expected = 1
    chain2 = N.Node(expected)
    chain1 = None

    result = A8.extend_chain(chain1, chain2)
    assert result.data == expected, "extend_chain returned unexpected data value, found {} expected {}".format(result.data, expected)


def test_extend_chain_singleton_content_3():
    """ Test extend_chain()
    """
    expected_1 = 1
    expected_2 = 2
    chain1 = N.Node(expected_1)
    chain2 = N.Node(expected_2)

    result = A8.extend_chain(chain1, chain2)
    assert result.data == expected_1, "extend_chain returned unexpected first data value, found {} expected {}".format(result.data, expected_1)
    assert result.next.data == expected_2, "extend_chain returned unexpected second data value, found {} expected {}".format(result.next.data, expected_2)


def test_extend_chain_multiple_content_4():
    """ Test extend_chain()
    """
    data_vals = [1, 3, 2, 4]
    chain1 = N.Node(data_vals[0], N.Node(data_vals[1]))
    chain2 = N.Node(data_vals[2], N.Node(data_vals[3]))

    result = A8.extend_chain(chain1, chain2)

    walker = result
    for i in range(4):
        assert walker.data == data_vals[i], 'extend_chain return unexpected value at index {}: found {}, expected {}'.format(i, walker.data, data_vals[i])
        walker = walker.next
        



#########################################################################
# testing for sort_chain()



def test_sort_chain_empty():
    """ Test sort_chain()
    """
    chain = None
    result = A8.sort_chain(chain)

    assert result is None, "sort_chain returned non-empty chain given empty input"


def test_sort_chain_singleton_structure():
    """ Test sort_chain()
    """
    chain = N.Node(1)
    result = A8.sort_chain(chain)

    assert result is not None, "sort_chain returned empty chain given singleton input"
    assert result.next is None, "sort_chain returned extended chain given singleton input"


def test_sort_chain_singleton_content():
    """ Test sort_chain()
    """
    expected = 1
    chain = N.Node(expected)
    result = A8.sort_chain(chain)

    assert result.data == 1, "sort_chain returned extraneous data given singleton input; expected {} found {}".format(expected, result.data)


def test_sort_chain_two_structure():
    """ Test sort_chain()
    """
    chain = N.Node(1, N.Node(2))
    result = A8.sort_chain(chain)

    assert result is not None, "sort_chain returned empty chain given input chain size 2 already in order"
    assert result.next is not None, "sort_chain returned singleton chain given input chain size 2 already in order"
    assert result.next.next is None, "sort_chain returned extended chain given input chain size 2 already in order"


def test_sort_chain_two_content():
    """ Test sort_chain()
    """
    chain = N.Node(1, N.Node(2))
    result = A8.sort_chain(chain)

    assert result.data <= result.next.data, "sort_chain returned chain out of order given input chain size 2 already in order"


def test_sort_chain_two_structure_2():
    """ Test sort_chain()
    """
    chain = N.Node(3, N.Node(2))
    result = A8.sort_chain(chain)

    assert result is not None, "sort_chain returned empty chain given input chain size 2 in reverse order"
    assert result.next is not None, "sort_chain returned singleton chain given input chain size 2 in reverse order"
    assert result.next.next is None, "sort_chain returned extended chain given input chain size 2 in reverse order"


def test_sort_chain_two_content_2():
    """ Test sort_chain()
    """
    chain = N.Node(3, N.Node(2))
    result = A8.sort_chain(chain)

    assert result.data <= result.next.data, "sort_chain returned chain out of order given input chain size 2 in reverse order"


def test_sort_chain_two_structure_3():
    """ Test sort_chain()
    """
    chain = N.Node(2, N.Node(2))
    result = A8.sort_chain(chain)

    assert result is not None, "sort_chain returned empty chain given input chain size 2 with dupicates"
    assert result.next is not None, "sort_chain returned singleton chain given input chain size 2 with dupicates"
    assert result.next.next is None, "sort_chain returned extended chain given input chain size 2 with dupicates"


def test_sort_chain_two_content_3():
    """ Test sort_chain()
    """
    chain = N.Node(2, N.Node(2))
    result = A8.sort_chain(chain)

    assert result.data <= result.next.data, "sort_chain returned chain out of order given input chain size 2 with dupicates"


def test_sort_chain_multiple_structure_increasing():
    """ Test sort_chain()
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
    test_split_chain_empty,
    test_split_chain_singleton_structure,
    test_split_chain_singleton_structure,
    test_split_chain_singleton_structure,
    test_split_chain_singleton_content_1,
    test_split_chain_singleton_content_2,
    test_split_chain_singleton_content_3,
    test_split_chain_two_structure_1,
    test_split_chain_two_structure_2,
    test_split_chain_two_structure_3,
    test_split_chain_two_structure_3,
    test_split_chain_two_structure_3,
    test_split_chain_two_content_1,
    test_split_chain_two_content_2,
    test_split_chain_two_content_3,
    test_split_chain_two_content_4,
    test_split_chain_two_content_5,
    test_split_chain_multiple_structure_1,
    test_split_chain_multiple_structure_2,
    test_split_chain_multiple_structure_3,
    test_split_chain_multiple_structure_4,
    test_split_chain_multiple_content_1,
    test_split_chain_multiple_content_2,
    test_split_chain_multiple_content_3,
    test_split_chain_multiple_content_4,
    test_extend_chain_empty,
    test_extend_chain_singleton_structure_1,
    test_extend_chain_singleton_structure_2,
    test_extend_chain_singleton_structure_3,
    test_extend_chain_multiple_structure_3,
    test_extend_chain_singleton_content_1,
    test_extend_chain_singleton_content_2,
    test_extend_chain_singleton_content_3,
    test_extend_chain_multiple_content_4,
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

