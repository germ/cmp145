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
#   A test script for selection.py sort


import a3q1 as sel

# UNIT TESTING
# testing sel.selection.py()


# Exercise: come up with test cases:
#   black box
#   white box
#   Equivalence classes
#   boundary cases
#
# Consider:
#   test case coverage
#   degree of coverage
#   unit/integration/system


test_item = 'selection_sort()'
data_1 = [3,1,2]
expected = [1,2,3]
reason = "short list un-ordered, biggest vluae first"

# call the operation
result = sel.selection_sort(data_1)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))




data_1 = [0,1,4]
expected = [0,1,4]
reason = "short list ordered increasing"

# call the operation
result = sel.selection_sort(data_1)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))



data_1 = [10, 5, 2]
expected = [2, 5, 10]
reason = "short list ordered, decreasing"

# call the operation
result = sel.selection_sort(data_1)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


data_1 = []
expected = []
reason = "empty lsit"

# call the operation
result = sel.selection_sort(data_1)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


data_1 = [4]
expected = [4]
reason = "list with one element"

# call the operation
result = sel.selection_sort(data_1)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


data_1 = [0,1]
expected = [0,1]
reason = "list of two incvreasing"

# call the operation
result = sel.selection_sort(data_1)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


data_1 = [4,1]
expected = [1,4]
reason = "list of two decreasing"

# call the operation
result = sel.selection_sort(data_1)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


data_1 = [1, 1, 1]
expected = [1, 1, 1]
reason = "short list all the same value"

# call the operation
result = sel.selection_sort(data_1)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))



print('Testing done!!!')