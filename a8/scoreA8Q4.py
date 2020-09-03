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
#     scoring script for A8Q4
#     student version
#
#     Run this script to see how many of your functions work!
#     

import node as N
import A8Q4 as A8

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

    score = [(4,0), (17, 3), (31,5), (39,6), (45,7), (46, 8)
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

    result_left, result_right = A8.split_chain(chain)

    assert result_left is None and result_right is None, "split_chain did not return empty chains on empty chain"


def test_split_chain_singleton_structure():
    """ Test split_chain()
    """
    chain = N.Node(1)

    result_left, result_right = A8.split_chain(chain)

    assert result_right is None, "split_chain did not return empty right chain on singleton chain"
    assert result_left is not None, "split_chain returned empty left chain on singleton chain"
    assert result_left.next is None, "split_chain returned badly formed left chain on singleton chain"


def test_split_chain_singleton_content():
    """ Test split_chain()
    """
    data = 1
    chain = N.Node(data)
    expected = data

    result_left, result_right = A8.split_chain(chain)

    assert result_left.data == expected, "split_chain: expected {} found {} in left chain on singleton chain".format(expected, result_left)


def test_split_chain_two_structure():
    """ Test split_chain()
    """
    data1 = 1
    data2 = 2
    chain = N.Node(data1, N.Node(data2))

    result_left, result_right = A8.split_chain(chain)

    assert result_right is not None, "split_chain returned empty right chain on chain length 2"
    assert result_left is not None, "split_chain returned empty left chain on chain length 2"
    assert result_left.next is None, "split_chain returned badly formed left chain on chain length 2"
    assert result_right.next is None, "split_chain returned badly formed right chain on chain length 2"


def test_split_chain_two_content():
    """ Test split_chain()
    """
    data1 = 1
    data2 = 2
    chain = N.Node(data1, N.Node(data2))

    result_left, result_right = A8.split_chain(chain)

    check_left = (result_left.data == data1) or (result_left.data == data2)
    check_right = (result_right.data == data1) or (result_right.data == data2)
    check_both = (result_left.data != result_right.data)
    assert check_left, "split_chain left data value {} not from original chain length 2".format(result_left.data)
    assert check_right, "split_chain right data value {} not from original chain length 2".format(result_right.data)
    assert check_both, "split_chain put same data value {} in both left and right on chain length 2".format(result_right.data)


def test_split_chain_multiple_structure_even():
    """ Test split_chain()
    """
    n = 5
    data = range(2*n)
    chain = None
    for item in data:
        chain = N.Node(item, chain)

    result_left, result_right = A8.split_chain(chain)

    walker = result_left
    for i in range(n):
        assert walker is not None, "split_chain returned short left chain for length {}, terminated at index {}".format(2*n, i)
        walker = walker.next

    assert walker is None, "split_chain returned left chain longer than length {}".format(n)

    walker = result_right
    for i in range(n):
        assert walker is not None, "split_chain returned short right chain for length {}, terminated at index {}".format(2*n, i)
        walker = walker.next

    assert walker is None, "split_chain returned right chain longer than length {}".format(n)


def test_split_chain_multiple_structure_odd():
    """ Test split_chain()
    """
    n = 5
    data = range(2*n+1)
    chain = None
    for item in data:
        chain = N.Node(item, chain)

    result_left, result_right = A8.split_chain(chain)

    walker = result_left
    for i in range(n):
        assert walker is not None, "split_chain returned short left chain for length {}, terminated at index {}".format(2*n, i)
        walker = walker.next

    assert walker is not None, "split_chain returned left chain terminated at length {}".format(n)
    assert walker is not None and walker.next is None, "split_chain returned left chain too long!  length {}".format(n)

    walker = result_right
    for i in range(n):
        assert walker is not None, "split_chain returned short right chain for length {}, terminated at index {}".format(2*n, i)
        walker = walker.next

    assert walker is None, "split_chain returned right chain longer than length {}".format(n)


def test_split_chain_multiple_content_even():
    """ Test split_chain()
    """
    n = 5
    data = range(2*n)
    chain = None
    for item in data:
        chain = N.Node(item, chain)

    result_left, result_right = A8.split_chain(chain)

    seen = [False]*len(data)
    walker = result_left
    while walker is not None:
        assert walker.data in data, "split_chain extraneous data value in left chain for length {}".format(2*n)
        seen[walker.data] = True
        walker = walker.next

    walker = result_right
    while walker is not None:
        assert walker.data in data, "split_chain extraneous data value in right chain for length {}".format(2*n)
        seen[walker.data] = True
        walker = walker.next

    for i,b in enumerate(seen):
        assert b, "split_chain omitted data value {}".format(i)


def test_split_chain_multiple_content_odd():
    """ Test split_chain()
    """
    n = 5
    data = range(2*n+1)
    chain = None
    for item in data:
        chain = N.Node(item, chain)

    result_left, result_right = A8.split_chain(chain)

    seen = [False]*len(data)
    walker = result_left
    while walker is not None:
        assert walker.data in data, "split_chain extraneous data value in left chain for length {}".format(2*n)
        seen[walker.data] = True
        walker = walker.next

    walker = result_right
    while walker is not None:
        assert walker.data in data, "split_chain extraneous data value in right chain for length {}".format(2*n)
        seen[walker.data] = True
        walker = walker.next

    for i,b in enumerate(seen):
        assert b, "split_chain omitted data value {}".format(i)



def text_merge_chain_LR_empty():
    """ Test merge_chain()
    """
    result = A8.merge_chain(None, None)
    assert result is None, "merge_chain failed on empty inputs"


def test_merge_chain_L_empty_structure():
    """ Test merge_chain()
    """
    right = N.Node(1)
    result = A8.merge_chain(None, right)
    assert result is not None, "merge_chain created empty chain given empty left input"


def test_merge_chain_L_empty_content():
    """ Test merge_chain()
    """
    right = N.Node(1)
    result = A8.merge_chain(None, right)
    assert result.data == right.data, "merge_chain created chain with extraneous data, expected {} found {}".format(right.data, result.data)


def test_merge_chain_R_empty_structure():
    """ Test merge_chain()
    """
    left = N.Node(1)
    result = A8.merge_chain(left, None)
    assert result is not None, "merge_chain created empty chain given empty right input"


def test_merge_chain_R_empty_content():
    """ Test merge_chain()
    """
    left = N.Node(1)
    result = A8.merge_chain(left, None)
    assert result.data == left.data, "merge_chain created chain with extraneous data, expected {} found {}".format(left.data, result.data)


def test_merge_chain_two_singleton_structure():
    """ Test merge_chain()
    """
    left = N.Node(1)
    right = N.Node(2)
    result = A8.merge_chain(left, right)
    assert result is not None, "merge_chain created empty chain given non-empty inputs"
    assert result.next is not None, "merge_chain created short chain given non-empty inputs"


def test_merge_chain_two_singleton_content():
    """ Test merge_chain()
    """
    left = N.Node(1)
    right = N.Node(2)
    result = A8.merge_chain(left, right)
    first = result.data
    second = result.next.data
    assert first <= second, "merge_chain put {} before {} given two singleton chains".format(first, second)


def test_merge_chain_one_singleton_L_structure():
    """ Test merge_chain()
    """
    left = N.Node(1)
    right = N.Node(2, N.Node(3))
    result = A8.merge_chain(left, right)
    assert result is not None, "merge_chain created empty chain given non-empty inputs"
    assert result.next is not None, "merge_chain created chain length 1 given node chains length 1, 2"
    assert result.next.next is not None, "merge_chain created chain length 2 given node chains length 1, 2"


def test_merge_chain_one_singleton_L_content():
    """ Test merge_chain()
    """
    left = N.Node(1)
    right = N.Node(2, N.Node(3))
    result = A8.merge_chain(left, right)

    first = result.data
    second = result.next.data
    third = result.next.next.data
    assert first <= second, "merge_chain put {} before {} given node chains length 1, 2".format(first, second)
    assert second <= third, "merge_chain put {} before {} given node chains length 1, 2".format(second, third)


def test_merge_chain_one_singleton_L_structure_2():
    """ Test merge_chain()
    """
    left = N.Node(2)
    right = N.Node(1, N.Node(3))
    result = A8.merge_chain(left, right)
    assert result is not None, "merge_chain created empty chain given non-empty inputs"
    assert result.next is not None, "merge_chain created chain length 1 given node chains length 1, 2"
    assert result.next.next is not None, "merge_chain created chain length 2 given node chains length 1, 2"


def test_merge_chain_one_singleton_L_content_2():
    """ Test merge_chain()
    """
    left = N.Node(2)
    right = N.Node(1, N.Node(3))
    result = A8.merge_chain(left, right)

    first = result.data
    second = result.next.data
    third = result.next.next.data
    assert first <= second, "merge_chain put {} before {} given node chains length 1, 2".format(first, second)
    assert second <= third, "merge_chain put {} before {} given node chains length 1, 2".format(second, third)


def test_merge_chain_one_singleton_L_structure_3():
    """ Test merge_chain()
    """
    left = N.Node(5)
    right = N.Node(1, N.Node(3))
    result = A8.merge_chain(left, right)
    assert result is not None, "merge_chain created empty chain given non-empty inputs"
    assert result.next is not None, "merge_chain created chain length 1 given node chains length 1, 2"
    assert result.next.next is not None, "merge_chain created chain length 2 given node chains length 1, 2"


def test_merge_chain_one_singleton_L_content_3():
    """ Test merge_chain()
    """
    left = N.Node(5)
    right = N.Node(1, N.Node(3))
    result = A8.merge_chain(left, right)

    first = result.data
    second = result.next.data
    third = result.next.next.data
    assert first <= second, "merge_chain put {} before {} given node chains length 1, 2".format(first, second)
    assert second <= third, "merge_chain put {} before {} given node chains length 1, 2".format(second, third)


def test_merge_chain_one_singleton_R_structure():
    """ Test merge_chain()
    """
    right = N.Node(1)
    left = N.Node(2, N.Node(3))
    result = A8.merge_chain(left, right)
    assert result is not None, "merge_chain created empty chain given non-empty inputs"
    assert result.next is not None, "merge_chain created chain length 1 given node chains length 1, 2"
    assert result.next.next is not None, "merge_chain created chain length 2 given node chains length 1, 2"


def test_merge_chain_one_singleton_R_content():
    """ Test merge_chain()
    """
    right = N.Node(1)
    left = N.Node(2, N.Node(3))
    result = A8.merge_chain(left, right)

    first = result.data
    second = result.next.data
    third = result.next.next.data
    assert first <= second, "merge_chain put {} before {} given node chains length 1, 2".format(first, second)
    assert second <= third, "merge_chain put {} before {} given node chains length 1, 2".format(second, third)


def test_merge_chain_one_singleton_R_structure_2():
    """ Test merge_chain()
    """
    right = N.Node(2)
    left = N.Node(1, N.Node(3))
    result = A8.merge_chain(left, right)
    assert result is not None, "merge_chain created empty chain given non-empty inputs"
    assert result.next is not None, "merge_chain created chain length 1 given node chains length 1, 2"
    assert result.next.next is not None, "merge_chain created chain length 2 given node chains length 1, 2"


def test_merge_chain_one_singleton_R_content_2():
    """ Test merge_chain()
    """
    right = N.Node(2)
    left = N.Node(1, N.Node(3))
    result = A8.merge_chain(left, right)

    first = result.data
    second = result.next.data
    third = result.next.next.data
    assert first <= second, "merge_chain put {} before {} given node chains length 1, 2".format(first, second)
    assert second <= third, "merge_chain put {} before {} given node chains length 1, 2".format(second, third)


def test_merge_chain_one_singleton_R_structure_3():
    """ Test merge_chain()
    """
    right = N.Node(5)
    left = N.Node(1, N.Node(3))
    result = A8.merge_chain(left, right)
    assert result is not None, "merge_chain created empty chain given non-empty inputs"
    assert result.next is not None, "merge_chain created chain length 1 given node chains length 1, 2"
    assert result.next.next is not None, "merge_chain created chain length 2 given node chains length 1, 2"


def test_merge_chain_one_singleton_R_content_3():
    """ Test merge_chain()
    """
    right = N.Node(5)
    left = N.Node(1, N.Node(3))
    result = A8.merge_chain(left, right)

    first = result.data
    second = result.next.data
    third = result.next.next.data
    assert first <= second, "merge_chain put {} before {} given node chains length 1, 2".format(first, second)
    assert second <= third, "merge_chain put {} before {} given node chains length 1, 2".format(second, third)


def test_merge_chain_longer_structure():
    """ Test merge_chain()
    """
    right = N.Node(2, N.Node(4, N.Node(5, N.Node(6, N.Node(10)))))
    left = N.Node(1, N.Node(3, N.Node(7, N.Node(8, N.Node(9)))))
    result = A8.merge_chain(left, right)

    walker = result
    count = 0
    while walker is not None:
        count += 1
        walker = walker.next
    expected = 10

    assert count == expected, "merge_chain created a short list, only {} elements, expected {}".format(count, expected)


def test_merge_chain_longer_content():
    """ Test merge_chain()
    """
    right = N.Node(1, N.Node(3, N.Node(4, N.Node(5, N.Node(9)))))
    left = N.Node(0, N.Node(2, N.Node(6, N.Node(7, N.Node(8)))))
    result = A8.merge_chain(left, right)

    data = range(10)
    seen = [False]*10
    walker = result
    while walker is not None:
        assert walker.data in data, "merge_chain added extraneous data, found data {}".format(walker.data)
        seen[walker.data] = True
        walker = walker.next
    for i,b in enumerate(seen):
        assert b, "merge_chain did not record data value {}".format(i)



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
    test_split_chain_singleton_content,
    test_split_chain_two_structure,
    test_split_chain_two_content,
    test_split_chain_multiple_structure_even,
    test_split_chain_multiple_structure_odd,
    test_split_chain_multiple_content_even,
    test_split_chain_multiple_content_odd,
    text_merge_chain_LR_empty,
    test_merge_chain_L_empty_structure,
    test_merge_chain_L_empty_content,
    test_merge_chain_R_empty_structure,
    test_merge_chain_R_empty_content,
    test_merge_chain_two_singleton_structure,
    test_merge_chain_two_singleton_content,
    test_merge_chain_one_singleton_L_structure,
    test_merge_chain_one_singleton_L_content,
    test_merge_chain_one_singleton_L_structure_2,
    test_merge_chain_one_singleton_L_content_2,
    test_merge_chain_one_singleton_L_structure_3,
    test_merge_chain_one_singleton_L_content_3,
    test_merge_chain_one_singleton_R_structure,
    test_merge_chain_one_singleton_R_content,
    test_merge_chain_one_singleton_R_structure_2,
    test_merge_chain_one_singleton_R_content_2,
    test_merge_chain_one_singleton_R_structure_3,
    test_merge_chain_one_singleton_R_content_3,
    test_merge_chain_longer_structure,
    test_merge_chain_longer_content,
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

