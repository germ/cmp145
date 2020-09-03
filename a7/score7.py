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
#     scoring script for A6
#     student version
#
#     Run this script to see how many of your functions work!
#     

import LList as L

verbose = False # change to False to reduce output

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

    score = [(107,0), (122,5), (142,10), (162, 15), (182,20), (202,24), (232,27), (236,30)]

    for (p,s) in score:
        if passed <= p:
            print('Passed:', passed, 'Resulting Grade:', s, 'out of 30')
            break
    return
    
###### A load of tests follows
# all the unit and integration tests


def test_create_initial_size():
    allist = L.LList()
    result = allist._size
    assert result == 0, "create(): Check size in new LList record; returned "+str(result)


def test_create_initial_head():
    allist = L.LList()
    result = allist._head 
    assert result is None, "create(): Check head in new LList record; returned "+str(result)


def test_create_initial_tail():
    allist = L.LList()
    result = allist._tail 
    assert result is None, "create(): Check tail in new LList record; returned "+str(result)


###############################################################################################
# UNIT TESTING - List.empty(), List.size()
###############################################################################################

def test_empty_empty():
    # create a record by hand
    thellist = L.LList()

    # check if is_empty() works
    result = thellist.is_empty()
    assert result , 'is_empty() on new LList record; returned '+str(result)


def test_empty_singleton():
    # create a node chain and list by hand
    thenode = L.node('arbitrary')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    # check if is_empty() works
    result = not thellist.is_empty()
    assert result , 'is_empty() on singleton LList; returned '+str(result)


def test_size_singleton():
    thenode = L.node('arbitrary')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode
    
    result = thellist.size() 
    assert result == 1, 'size() on singleton LList; returned '+str(result)


###############################################################################################
# UNIT TESTING - List.add_to_front()
###############################################################################################

def test_add_to_front_size_1():
    thellist = L.LList()
    target = 'one'
    thellist.add_to_front(target)
    result = thellist._size 
    assert result == 1, 'add_to_front(): check size after insertion on empty LList; returned '+str(result)


def test_add_to_front_head_1():
    thellist = L.LList()
    target = 'one'
    thellist.add_to_front(target)
    result = thellist._head 
    assert result is not None, 'add_to_front() check head after insertion on empty LList; head not set correctly'


def test_add_to_front_tail_1():
    thellist = L.LList()
    target = 'one'
    thellist.add_to_front(target)
    result = thellist._tail 
    assert result is not None, 'add_to_front() check head after insertion on empty LList; tail not set correctly'


def test_add_to_front_refs_1():
    thellist = L.LList()
    target = 'one'
    thellist.add_to_front(target)
    result = thellist._head 
    assert result is thellist._tail, 'add_to_front() check head, tail after insertion on empty LList; head tail refs should be same but are not'


def test_add_to_front_data_1():
    thellist = L.LList()
    target = 'one'
    thellist.add_to_front(target)
    result = thellist._head.data
    assert result is target, 'add_to_front() check data at head after insertion on empty LList; data set to '+str(result)+' but should be '+"'"+str(target)+"'"


def test_add_to_front_data_2():
    thellist = L.LList()
    target = 'one'
    thellist.add_to_front(target)
    result = thellist._tail.data
    assert result is target, 'add_to_front() check data at tail after insertion on empty LList; data set to '+str(result)+' but should be '+"'"+str(target)+"'"


def test_add_to_front_end_1():
    thellist = L.LList()
    target = 'one'
    thellist.add_to_front(target)
    result = thellist._head.next
    assert result is None, 'add_to_front() check node chain after insertion on empty LList: chain should end at one node, but next is not None!'


def test_add_to_front_empty_1():
    thellist = L.LList()
    target = 'one'
    thellist.add_to_front(target)
    result = not thellist.is_empty()
    assert result , 'add_to_front() check is_empty() after insertion on empty LList: is_empty() returned True'


###############################################################################################
# UNIT TESTING - List.add_to_front()
###############################################################################################

def test_add_to_front_size_2():
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'two'
    thellist.add_to_front(target)
    result = thellist._size 
    assert result == 2, 'add_to_front()  on LList with one node: size not set correctly'


def test_add_to_front_head_2():
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'two'
    thellist.add_to_front(target)
    result = thellist._head 
    assert result is not thenode, 'add_to_front()  on LList with one node: head not set correctly'


def test_add_to_front_tail_2():
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'two'
    thellist.add_to_front(target)
    result = thellist._tail 
    assert result is thenode, 'add_to_front()  on LList with one node: tail not set correctly'


def test_add_to_front_refs_2():
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'two'
    thellist.add_to_front(target)
    result = thellist._head 
    assert result != thellist._tail, 'add_to_front()  on LList with one node: head tail refs equal'


def test_add_to_front_data_3():
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'two'
    thellist.add_to_front(target)
    result = thellist._head.data
    assert result == target, 'add_to_front()  on LList with one node: data not set correctly in head'


def test_add_to_front_chain_2():
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'two'
    thellist.add_to_front(target)
    result = thellist._head.next
    assert result is not None, 'add_to_front()  on LList with one node: chain should not end at one node'


def test_add_to_front_chain_3():
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'two'
    thellist.add_to_front(target)
    result = thellist._head.next
    assert result is thenode, 'add_to_front()  on LList with one node: new node should point to existing node'


def test_add_to_front_data_4():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'two'
    thellist.add_to_front(target)
    result = thellist._tail.data
    assert result == tail_data, 'add_to_front()  on LList with one node: data not set correctly in tail'


def test_add_to_front_empty_2():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'two'
    thellist.add_to_front(target)
    result = not thellist.is_empty()
    assert result , 'add_to_front() on LList with one node; is_empty() returned True'


def test_add_to_front_size_3():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'two'
    thellist.add_to_front(target)
    result = thellist.size() 
    assert result == 2, 'add_to_front()  on LList with one node: size() not returning correct value'


###############################################################################################
# UNIT TESTING - List.add_to_back()
###############################################################################################

def test_add_to_back_head_1():
    thellist = L.LList()
    target = 'three'
    thellist.add_to_back(target)
    result = thellist._head 
    assert result is not None, 'add_to_back() check head after insertion on empty LList: head not set correctly'


def test_add_to_back_tail_1():
    thellist = L.LList()
    target = 'three'
    thellist.add_to_back(target)
    result = thellist._tail 
    assert result is not None, 'add_to_back() check tail after insertion on empty LList: tail not set correctly'


def test_add_to_back_size_1():
    thellist = L.LList()
    target = 'three'
    thellist.add_to_back(target)
    result = thellist._size 
    assert result == 1, 'add_to_back() check size after insertion on empty LList: size not set correctly'


def test_add_to_back_refs_1():
    thellist = L.LList()
    target = 'three'
    thellist.add_to_back(target)
    result = thellist._head 
    assert result == thellist._tail, 'add_to_back() check head, tail after insertion on empty LList: head tail refs different'


def test_add_to_back_data_1():
    thellist = L.LList()
    target = 'three'
    thellist.add_to_back(target)
    result = thellist._head.data
    assert result == target, 'add_to_back() check data at head after insertion on empty LList: data not set correctly in head'


def test_add_to_back_data_2():
    thellist = L.LList()
    target = 'three'
    thellist.add_to_back(target)
    result = thellist._tail.data
    assert result == target, 'add_to_back() check data at tail after insertion on empty LList: data not set correctly in tail'


def test_add_to_back_chain_1():
    thellist = L.LList()
    target = 'three'
    thellist.add_to_back(target)
    result = thellist._head.next
    assert result is None, 'add_to_back() check node chain after insertion on empty LList: chain should end at one node'


def test_add_to_back_empty_1():
    thellist = L.LList()
    target = 'three'
    thellist.add_to_back(target)
    result = not thellist.is_empty()
    assert result , 'add_to_back() check is_empty() after insertion on empty LList: is_empty() returned True'


def test_add_to_back_size_2():
    thellist = L.LList()
    target = 'three'
    thellist.add_to_back(target)
    result = thellist.size() 
    assert result == 1, 'add_to_back() check size after insertion on empty LList: size() returned '+str(result)


###############################################################################################
# UNIT TESTING - List.add_to_back()
###############################################################################################

def test_add_to_back_size_3():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'four'
    thellist.add_to_back(target)
    result = thellist._size 
    assert result == 2, 'add_to_back() on LList with one node: size not set correctly'


def test_add_to_back_head_2():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'four'
    thellist.add_to_back(target)
    result = thellist._head 
    assert result is thenode, 'add_to_back()  on LList with one node: head not set correctly'


def test_add_to_back_tail_2():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'four'
    thellist.add_to_back(target)
    result = thellist._tail 
    assert result is not None, 'add_to_back()  on LList with one node: tail not set correctly'


def test_add_to_back_tail_3():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'four'
    thellist.add_to_back(target)
    result = thellist._tail 
    assert result is not thenode, 'add_to_back()  on LList with one node: tail should be the new node, but is not'


def test_add_to_back_refs_2():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'four'
    thellist.add_to_back(target)
    result = thellist._head 
    assert result != thellist._tail, 'add_to_back() on LList with one node: head tail refs equal, but should not'


def test_add_to_back_data_3():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'four'
    thellist.add_to_back(target)
    result = thellist._tail.data
    assert result == target, 'add_to_back() on LList with one node: data not set correctly in tail; should be '+str(target)+'but found '+str(result)


def test_add_to_back_data_4():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'four'
    thellist.add_to_back(target)
    result = thellist._head.data
    assert result != target, 'add_to_back() on LList with one node: data not set correctly in head; should be '+str(target)+'but found '+str(result)


def test_add_to_back_chain_2():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'four'
    thellist.add_to_back(target)
    result = thellist._head.next
    assert result is not None, 'add_to_back() on LList with one node: chain ended at one node, but should not'


def test_add_to_back_empty_2():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'four'
    thellist.add_to_back(target)
    result = not thellist.is_empty()
    assert result , 'add_to_back() on LList with one node: is_empty() returned True but should not'


def test_add_to_back_size_4():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'four'
    thellist.add_to_back(target)
    result = thellist.size() 
    assert result == 2, 'add_to_back() on LList with one node: size() returned '+str(result)


###############################################################################################
# UNIT TESTING - List.value_is_in()
###############################################################################################

def test_value_is_in_empty():
    thellist = L.LList()
    target = 5
    result = thellist.value_is_in(target) 
    assert result is False, 'value_is_in() on empty LList; returned True but should not'


def test_value_is_in_false_1():
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'six'
    result = thellist.value_is_in(target) 
    assert result is False, 'value_is_in() on singleton LList, target not present; returned True but should not'


def test_value_is_in_true_1():
    target = '7'
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    result = thellist.value_is_in(target) 
    assert result is True, 'value_is_in() on singleton LList, target present; returned False but should not'


def test_value_is_in_false_2():
    target = '7'
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    result = thellist.value_is_in(target) 
    assert result is False, 'value_is_in() on LList with 2 nodes, target not present; returned True but should not'


def test_value_is_in_true_2():
    target = '7'
    thetail = L.node(target)
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    
    result = thellist.value_is_in(target) 
    assert result is True, 'value_is_in() on LList with 2 nodes, target in tail; returned False but should not'


def test_value_is_in_true_3():
    target = '7'
    thetail = L.node('not the target')
    thehead = L.node(target, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    result = thellist.value_is_in(target) 
    assert result is True, 'value_is_in() on LList with 2 nodes, target in head; returned False but should not'


###############################################################################################
# UNIT TESTING - List.get_index_of_value()
###############################################################################################

def test_get_index_of_value_empty_flag_1():
    thellist = L.LList()
    target = 9
    flag, idx = thellist.get_index_of_value(target)
    result = flag 
    assert result is False, 'get_index_of_value() on empty LList; returned True but should not'


def test_get_index_of_value_empty_idx_1():
    thellist = L.LList()
    target = 9
    flag, idx = thellist.get_index_of_value(target)
    result = idx 
    assert result is None, 'get_index_of_value() on empty LList; returned index that is not None'


def test_get_index_of_value_notempty_flag_1():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'six'
    flag, idx = thellist.get_index_of_value(target)
    result = flag 
    assert result is False, 'get_index_of_value() on singleton LList, target not present: returned True but should not'


def test_get_index_of_value_notempty_idx_1():
    tail_data = 'not the target'
    thenode = L.node(tail_data)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    target = 'six'
    flag, idx = thellist.get_index_of_value(target)
    result = idx 
    assert result is None, 'get_index_of_value() on singleton LList, target not present: returned non-None index'


def test_get_index_of_value_notempty_flag_2():
    target = '10'
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode
    
    flag, idx = thellist.get_index_of_value(target)
    result = flag 
    assert result is True, 'get_index_of_value() on singleton LList, target present: returned False but should not'


def test_get_index_of_value_notempty_idx_2():
    target = '10'
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, idx = thellist.get_index_of_value(target)
    result = idx 
    assert result == 0, 'get_index_of_value() on singleton LList, target present: returned index '+str(result)+', should be 0'


def test_get_index_of_value_notempty_flag_3():
    target = '10'
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    
    flag, idx = thellist.get_index_of_value(target)
    result = flag 
    assert result is False, 'get_index_of_value() on LList with 2 nodes, target not present: returned True'


def test_get_index_of_value_notempty_idx_3():
    target = '10'
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    flag, idx = thellist.get_index_of_value(target)
    result = idx 
    assert result is None, 'get_index_of_value() on LList with 2 nodes, target not present: returned non-None index'


def test_get_index_of_value_notempty_flag_4():
    target = '10'
    thetail = L.node(target)
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    
    flag, idx = thellist.get_index_of_value(target)
    result = flag 
    assert result is True, 'get_index_of_value() on LList with 2 nodes, target in tail: returned False'


def test_get_index_of_value_notempty_idx_4():
    target = '10'
    thetail = L.node(target)
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    flag, idx = thellist.get_index_of_value(target)
    result = idx 
    assert result == 1, 'get_index_of_value() on LList with 2 nodes, target in tail: returned incorrect index '+str(result)


def test_get_index_of_value_notempty_flag_5():
    target = '10'
    thetail = L.node('not the target')
    thehead = L.node(target, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    flag, idx = thellist.get_index_of_value(target)
    result = flag 
    assert result is True, 'get_index_of_value() on LList with 2 nodes, target in head: returned False'


def test_get_index_of_value_notempty_idx_5():
    target = '10'
    thetail = L.node('not the target')
    thehead = L.node(target, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    flag, idx = thellist.get_index_of_value(target)
    result = idx 
    assert result == 0, 'get_index_of_value() on LList with 2 nodes, target in head: returned incorrect index '+str(result)


###############################################################################################
# UNIT TESTING - List.retrieve_data_at_index()
###############################################################################################

def test_retrieve_data_at_flag_1():
    thellist = L.LList()
    idx = 0
    flag, val = thellist.retrieve_data_at_index(idx)
    result = flag 
    assert result is False, 'retrieve_data_at_index() on empty LList: returned True but should not'


def test_retrieve_data_at_val_1():
    thellist = L.LList()
    idx = 0
    flag, val = thellist.retrieve_data_at_index(idx)
    result = val 
    assert result is None, 'retrieve_data_at_index() on empty LList: returned non-None value'


def test_retrieve_data_at_flag_2():
    target = 12
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode
    idx = 0
    flag, val = thellist.retrieve_data_at_index(idx)
    result = flag 
    assert result is True, 'retrieve_data_at_index() on singleton LList, valid index; returned False but should not'


def test_retrieve_data_at_val_2():
    target = 12
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode
    idx = 0
    flag, val = thellist.retrieve_data_at_index(idx)
    result = val 
    assert result == target, 'retrieve_data_at_index() on singleton LList, valid index; returned '+str(result)+' instead of '+str(target)


def test_retrieve_data_at_flag_3():
    thetail = L.node(16)
    thehead = L.node(18, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    
    idx = 0
    flag, val = thellist.retrieve_data_at_index(idx)
    result = flag 
    assert result is True, 'retrieve_data_at_index() on LList with two nodes, index 0: returned False but should not'


def test_retrieve_data_at_val_3():
    target = 18
    thetail = L.node(16)
    thehead = L.node(target, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    
    idx = 0
    flag, val = thellist.retrieve_data_at_index(idx)
    result = val 
    assert result == target, 'retrieve_data_at_index(): on LList with two nodes, index 0; returned data value '+str(result)+' instead of '+str(target)


def test_retrieve_data_at_flag_4():
    thetail = L.node(16)
    thehead = L.node(18, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 1
    flag, val = thellist.retrieve_data_at_index(idx)
    result = flag 
    assert result is True, 'retrieve_data_at_index(): on LList with two nodes, index 1: returned False but should not'


def test_retrieve_data_at_val_4():
    thetail = L.node(16)
    thehead = L.node(18, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 1
    flag, val = thellist.retrieve_data_at_index(idx)
    result = val 
    assert result == 16, 'retrieve_data_at_index(): on LList with two nodes, index 0; returned data value '+str(result)+' instead of '+str(target)


def test_retrieve_data_at_flag_5():
    thetail = L.node(16)
    thehead = L.node(18, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 2
    flag, val = thellist.retrieve_data_at_index(idx)
    result = flag 
    assert result is False, 'retrieve_data_at_index(): on LList with two nodes, invalid positive index; returned True but should not'


def test_retrieve_data_at_val_5():
    thetail = L.node(16)
    thehead = L.node(18, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 2
    flag, val = thellist.retrieve_data_at_index(idx)
    result = val 
    assert result is None, 'retrieve_data_at_index(): on LList with two nodes, invalid positive index; returned non-None value'


###############################################################################################
# UNIT TESTING - List.set_data_at_index()
###############################################################################################

def test_set_data_at_index_empty():
    thellist = L.LList()
    idx = 0
    target = 23
    flag = thellist.set_data_at_index(idx, target)
    result = flag 
    assert result is False, 'set_data_at_index() on empty LList; returned True but should not'


def test_set_data_at_index_notempty_flag_1():
    target = 23
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    idx = 0
    flag = thellist.set_data_at_index(idx, target)
    result = flag 
    assert result is True, 'set_data_at_index() on singleton LList, valid index; returned False but should not'


def test_set_data_at_index_notempty_data_1():
    target = 23
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    idx = 0
    flag = thellist.set_data_at_index(idx, target)
    result = thellist._head.data
    assert result == target, 'set_data_at_index() on singleton LList, valid index; data not set correctly'


def test_set_data_at_index_notempty_flag_2():
    target = 23
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 0
    flag = thellist.set_data_at_index(idx, target)
    result = flag 
    assert result is True, 'set_data_at_index() on LList with 2 nodes, index 0; returned False but should not'


def test_set_data_at_index_notempty_data_2():
    target = 23
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 0
    flag = thellist.set_data_at_index(idx, target)
    result = thellist._head.data
    assert result == target, 'set_data_at_index() on LList with 2 nodes, index 0; data not set correctly'


def test_set_data_at_index_notempty_flag_3():
    target = 23
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 1
    flag = thellist.set_data_at_index(idx, target)
    result = flag 
    assert result is True, 'set_data_at_index() on LList with 2 nodes, index 1; returned False but should not'


def test_set_data_at_index_notempty_data_3():
    target = 23
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 1
    flag = thellist.set_data_at_index(idx, target)
    result = thellist._tail.data
    assert result == target, 'set_data_at_index() on LList with 2 nodes, index 1; data not set correctly'


def test_set_data_at_index_notempty_flag_4():
    target = 23
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 2
    flag = thellist.set_data_at_index(idx, target)
    result = flag 
    assert result is False, 'set_data_at_index() on LList with 2 nodes, invalid positive index; returned True but should not'


def test_set_data_at_index_notempty_data_4():
    target = 23
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 2
    flag = thellist.set_data_at_index(idx, target)
    result = thellist._head.data
    assert result == 'not the target', 'set_data_at_index() on LList with 2 nodes, invalid positive index; data at head changed incorrectly'


def test_set_data_at_index_notempty_data_5():
    target = 23
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    idx = 2
    flag = thellist.set_data_at_index(idx, target)
    result = thellist._tail.data
    assert result == 'not the target', 'set_data_at_index() on LList with 2 nodes, invalid positive index; data at tail changed incorrectly'


###############################################################################################
# UNIT TESTING - List.remove_from_front()
###############################################################################################

def test_remove_from_front_empty_1():
    thellist = L.LList()
    flag, val = thellist.remove_from_front()
    result = flag 
    assert result is False, 'remove_from_front() on empty LList: returned True but should not'


def test_remove_from_front_empty_2():
    thellist = L.LList()
    flag, val = thellist.remove_from_front()
    result = val 
    assert result is None, 'remove_from_front() on empty LList: returned non-None value'


def test_remove_from_front_singleton_in_flag_1():
    target = 25
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, val = thellist.remove_from_front()
    result = flag 
    assert result is True, 'remove_from_front() on singleton LList: returned False but should not'


def test_remove_from_front_singleton_in_val_1():
    target = 25
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, val = thellist.remove_from_front()
    result = val 
    assert result == target, 'remove_from_front() on singleton LList: returned '+str(result)+' instead of '+str(target)


def test_remove_from_front_singleton_in_size_1():
    target = 25
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, val = thellist.remove_from_front()
    result = thellist._size 
    assert result == 0, 'remove_from_front() on singleton LList: incorrect size'


def test_remove_from_front_singleton_in_ref_head_1():
    target = 25
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, val = thellist.remove_from_front()
    result = thellist._head 
    assert result is None, 'remove_from_front() on singleton LList: head set incorrectly; should be None'

def test_remove_from_front_singleton_in_ref_tail_1():
    target = 25
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, val = thellist.remove_from_front()
    result = thellist._tail 
    assert result is None, 'remove_from_front() on singleton LList: tail set incorrectly; should be None'


def test_remove_from_front_notempty_in_flag_2():
    thetail = L.node(29)
    thehead = L.node(33, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    target = 33
    flag, val = thellist.remove_from_front()
    result = flag 
    assert result is True, 'remove_from_front() on LList with 2 nodes; returned False but should not'


def test_remove_from_front_notempty_in_val_2():
    thetail = L.node(29)
    thehead = L.node(33, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    target = 33
    flag, val = thellist.remove_from_front()
    result = val 
    assert result == target, 'remove_from_front() on LList with 2 nodes; returned '+str(result)+' instead of '+str(target)


def test_remove_from_front_notempty_in_size_2():
    thetail = L.node(29)
    thehead = L.node(33, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    target = 33
    flag, val = thellist.remove_from_front()
    result = thellist._size 
    assert result == 1, 'remove_from_front() on LList with 2 nodes; set incorrect size'


def test_remove_from_front_notempty_in_ref_head_2():
    thetail = L.node(29)
    thehead = L.node(33, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    flag, val = thellist.remove_from_front()
    result = thellist._head 
    assert result is thetail, 'remove_from_front() on LList with 2 nodes; head should be same as tail'

def test_remove_from_front_notempty_in_ref_tail_2():
    thetail = L.node(29)
    thehead = L.node(33, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    flag, val = thellist.remove_from_front()
    result = thellist._tail 
    assert result is thetail, 'remove_from_front() on LList with 2 nodes; tail should not have changed'


###############################################################################################
# UNIT TESTING - List.remove_from_back()
###############################################################################################

def test_remove_from_back_empty_flag():
    thellist = L.LList()
    flag, val = thellist.remove_from_back()
    result = flag 
    assert result is False, 'remove_from_back(): returned True for empty list'


def test_remove_from_back_empty_val():
    thellist = L.LList()
    flag, val = thellist.remove_from_back()
    result = val 
    assert result is None, 'remove_from_back(): returned non-None value for empty list'


def test_remove_from_back_singleton_flag():
    target = 25
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, val = thellist.remove_from_back()
    result = flag 
    assert result is True, 'remove_from_back():  returned False for singleton list'


def test_remove_from_back_singleton_val():
    target = 25
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, val = thellist.remove_from_back()
    result = val 
    assert result == target, 'remove_from_back():  returned incorrect value for singleton list'


def test_remove_from_back_singleton_size():
    target = 25
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, val = thellist.remove_from_back()
    result = thellist._size 
    assert result == 0, 'remove_from_back():  set incorrect size for singleton list'


def test_remove_from_back_singleton_in_ref_head_1():
    target = 25
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, val = thellist.remove_from_back()
    result = thellist._head 
    assert result is None, 'remove_from_back() on singleton LList: head set incorrectly; should be None'


def test_remove_from_back_singleton_in_ref_tail_1():
    target = 25
    thenode = L.node(target)
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode

    flag, val = thellist.remove_from_back()
    result = thellist._tail 
    assert result is None, 'remove_from_back() on singleton LList: tail set incorrectly; should be None'


def test_remove_from_back_multiple_flag():
    thetail = L.node(29)
    thehead = L.node(33, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    target = 29
    flag, val = thellist.remove_from_back()
    result = flag 
    assert result is True, 'remove_from_back():  returned False for list size 2'


def test_remove_from_back_multiple_val():
    thetail = L.node(29)
    thehead = L.node(33, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    target = 29
    flag, val = thellist.remove_from_back()
    result = val 
    assert result == target, 'remove_from_back():  returned incorrect value for list size 2'


def test_remove_from_back_multiple_size():
    thetail = L.node(29)
    thehead = L.node(33, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    target = 29
    flag, val = thellist.remove_from_back()
    result = thellist._size 
    assert result == 1, 'remove_from_back():  set incorrect size for list size 2'


def test_remove_from_back_multiple_in_ref_head_2():
    thetail = L.node(29)
    thehead = L.node(33, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    flag, val = thellist.remove_from_back()
    result = thellist._head 
    assert result is thehead, 'remove_from_back() on LList with 2 nodes; head should not have changed'

def test_remove_from_back_multiple_in_ref_tail_2():
    thetail = L.node(29)
    thehead = L.node(33, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    flag, val = thellist.remove_from_back()
    result = thellist._tail 
    assert result is thehead, 'remove_from_back() on LList with 2 nodes; tail should be the same as head'



###############################################################################################
# UNIT TESTING - List.insert_value_at_index()
###############################################################################################


def test_insert_value_at_index_empty_flag():
    thellist = L.LList()
    idx = 0
    target = 'one'
    flag = thellist.insert_value_at_index(target, idx)
    result = flag 
    assert result is True, 'insert_value_at_index() returned False for empty list'


def test_insert_value_at_index_empty_size():
    thellist = L.LList()
    idx = 0
    target = 'one'
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._size 
    assert result == 1, 'insert_value_at_index() set incorrect size for empty list'


def test_insert_value_at_index_empty_refs():
    thellist = L.LList()
    idx = 0
    target = 'one'
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._head 
    assert result == thellist._tail, 'insert_value_at_index()  head tail refs different'


def test_insert_value_at_index_empty_data_1():
    thellist = L.LList()
    idx = 0
    target = 'one'
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._head.data
    assert result == target, 'insert_value_at_index() data not set correctly'


def test_insert_value_at_index_empty_data_2():
    thellist = L.LList()
    idx = 0
    target = 'one'
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._tail.data
    assert result == target, 'insert_value_at_index() data not set correctly'


def test_insert_value_at_index_empty_chain():
    thellist = L.LList()
    idx = 0
    target = 'one'
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._head.next
    assert result is None, 'insert_value_at_index() chain should end at one node'


def test_insert_value_at_index_singleton_flag():
    target = 'two'
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode
    idx = 0
    flag = thellist.insert_value_at_index(target, idx)
    result = flag 
    assert result is True, 'insert_value_at_index() returned False for singleton list (valid index)'


def test_insert_value_at_index_singleton_data():
    target = 'two'
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode
    idx = 0
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._head.data
    assert result == target, 'insert_value_at_index() value not inserted correctly for singleton list (index = 0)'


def test_insert_value_at_index_singleton_chain_1():
    target = 'two'
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode
    idx = 0
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._head.next
    assert result is not None, 'insert_value_at_index() chain should have 2 nodes now'


def test_insert_value_at_index_singleton_size():
    target = 'two'
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode
    idx = 0
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._size 
    assert result == 2, 'insert_value_at_index() set incorrect size for singleton list'


def test_insert_value_at_index_singleton_refs_1():
    target = 'two'
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode
    idx = 0
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._head 
    assert result != thellist._tail, 'insert_value_at_index() head tail refs are equal'


def test_insert_value_at_index_singleton_refs_2():
    target = 'two'
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode
    idx = 0
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._tail.next
    assert result is None, 'insert_value_at_index() tail should have next == None'


def test_insert_value_at_index_singleton_flag_2():
    target = 'three'
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode
    idx = 1
    flag = thellist.insert_value_at_index(target, idx)
    result = flag 
    assert result is True, 'insert_value_at_index() : returned False for singleton list (valid index)'


def test_insert_value_at_index_singleton_data_2():
    target = 'three'
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode
    idx = 1
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._head.data
    assert result != target, 'insert_value_at_index() : head value set incorrectly for singleton list (index = 1)'


def test_insert_value_at_index_singleton_data_3():
    target = 'three'
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode
    idx = 1
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._tail.data
    assert result == target, 'insert_value_at_index() : value not inserted correctly for singleton list (index = 1)'


def test_insert_value_at_index_singleton_chain_3():
    target = 'three'
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode
    idx = 1
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._head.next
    assert result is not None, 'insert_value_at_index() : chain should have 2 nodes now!'


def test_insert_value_at_index_singleton_size_2():
    target = 'three'
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode
    idx = 1
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._size 
    assert result == 2, 'insert_value_at_index() set incorrect size for singleton list'


def test_insert_value_at_index_singleton_refs_3():
    target = 'three'
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode
    idx = 1
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._head 
    assert result != thellist._tail, 'insert_value_at_index() head tail refs are equal'


def test_insert_value_at_index_singleton_chain_2():
    target = 'three'
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode
    idx = 1
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._tail.next
    assert result is None, 'insert_value_at_index() tail should have next == None'


def test_insert_value_at_index_singleton_invalid_flag():
    target = 'four'
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode
    idx = 2
    flag = thellist.insert_value_at_index(target, idx)
    result = flag 
    assert result is False, 'insert_value_at_index() returned True for singleton list but invlaid index'


def test_insert_value_at_index_singleton_invalid_size():
    target = 'four'
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode
    idx = 2
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._size 
    assert result == 1, 'insert_value_at_index() changed size for for singleton list but invalid index'


def test_insert_value_at_index_singleton_invalid_refs():
    target = 'four'
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    thellist._tail = thenode
    idx = 2
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._head 
    assert result == thellist._tail, 'insert_value_at_index() head tail refs changed on invalid index'


def test_insert_value_at_index_multiple_flag_1():
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    target = 'five'
    idx = 0
    flag = thellist.insert_value_at_index(target, idx)
    result = flag 
    assert result is True, 'insert_value_at_index() : returned False for list size 2 (valid index)'


def test_insert_value_at_index_multiple_data_1():
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    target = 'five'
    idx = 0
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._head.data
    assert result == target, 'insert_value_at_index() : value not inserted correctly for list size 2 (index = 0)'


def test_insert_value_at_index_multiple_size_1():
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    target = 'five'
    idx = 0
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._size 
    assert result == 3, 'insert_value_at_index() : set incorrect size for list size 2'


def test_insert_value_at_index_multiple_chain_1():
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    target = 'five'
    idx = 0
    result = thellist._tail.next
    assert result is None, 'insert_value_at_index() : list size 2, tail should have next == None'


def test_insert_value_at_index_multiple_flag_2():
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    target = 'six'
    idx = 1
    flag = thellist.insert_value_at_index(target, idx)
    result = flag 
    assert result is True, 'insert_value_at_index() returned False for list size 2 (valid index)'


def test_insert_value_at_index_multiple_data_2():
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    target = 'six'
    idx = 1
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._head.data
    assert result != target, 'insert_value_at_index() value not inserted correctly for list size 2 (index = 1)'


def test_insert_value_at_index_multiple_data_3():
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    target = 'six'
    idx = 1
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._head.next.data
    assert result == target, 'insert_value_at_index() value not inserted correctly for list size 2 (index = 1)'


def test_insert_value_at_index_multiple_size_2():
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    target = 'six'
    idx = 1
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._size 
    assert result == 3, 'insert_value_at_index() : set incorrect size for list size 2'


def test_insert_value_at_index_multiple_chain_2():
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    target = 'six'
    idx = 1
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._tail.next
    assert result is None, 'insert_value_at_index() : list size 2, tail should have next == None'


def test_insert_value_at_index_flag_3():
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    target = 'nine'
    idx = 2
    flag = thellist.insert_value_at_index(target, idx)
    result = flag 
    assert result is True, 'insert_value_at_index() : returned False for list size 2 (valid index)'


def test_insert_value_at_index_data_4():
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    target = 'nine'
    idx = 2
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._head.data
    assert result != target, 'insert_value_at_index() value not inserted correctly for list size 2 (index = 2)'


def test_insert_value_at_index_data_5():
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    target = 'nine'
    idx = 2
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._head.next.data
    assert result != target, 'insert_value_at_index() value not inserted correctly for list size 2 (index = 2)'


def test_insert_value_at_index_data_6():
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    target = 'nine'
    idx = 2
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._tail.data
    assert result == target, 'insert_value_at_index() value not inserted correctly for list size 2 (index = 2)'


def test_insert_value_at_index_size_3():
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    target = 'nine'
    idx = 2
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._size 
    assert result == 3, 'insert_value_at_index() set incorrect size for list size 2'


def test_insert_value_at_index_chain_3():
    thetail = L.node('not the target')
    thehead = L.node('not the target', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    target = 'nine'
    idx = 2
    flag = thellist.insert_value_at_index(target, idx)
    result = thellist._tail.next
    assert result is None, 'insert_value_at_index() list size 2, tail should have next == None'


###############################################################################################
# UNIT TESTING - List.delete_item_at_index()
###############################################################################################

def test_delete_item_at_index_empty_flag():
    thellist = L.LList()
    idx = 0
    flag = thellist.delete_item_at_index( idx)
    result = flag 
    assert result is False, 'delete_item_at_index() returned True for empty list'


def test_delete_item_at_index_empty_size():
    thellist = L.LList()
    idx = 0
    flag = thellist.delete_item_at_index( idx)
    result = thellist._size 
    assert result == 0, 'delete_item_at_index() set incorrect size for empty list'


def test_delete_item_at_index_empty_refs():
    thellist = L.LList()
    idx = 0
    flag = thellist.delete_item_at_index( idx)
    result = thellist._head 
    assert result == thellist._tail, 'delete_item_at_index() head tail refs different'


def test_delete_item_at_index_singleton_flag():
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    idx = 0
    flag = thellist.delete_item_at_index( idx)
    result = flag 
    assert result is True, 'delete_item_at_index() returned False for singleton list (valid index)'


def test_delete_item_at_index_singleton_head():
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    idx = 0
    flag = thellist.delete_item_at_index( idx)
    result = thellist._head 
    assert result is None, 'delete_item_at_index() value not deleted correctly for singleton list (index = 0)'


def test_delete_item_at_index_singleton_size():
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    idx = 0
    flag = thellist.delete_item_at_index( idx)
    result = thellist._size 
    assert result == 0, 'delete_item_at_index() set incorrect size for singleton list'


def test_delete_item_at_index_singleton_tail():
    thenode = L.node('not the target')
    thellist = L.LList()
    thellist._size = 1
    thellist._head = thenode
    idx = 0
    flag = thellist.delete_item_at_index( idx)
    result = thellist._tail 
    assert result is None, 'delete_item_at_index() tail should be None'


def test_delete_item_at_index_multiple_flag_1():
    thetail = L.node('ten')
    thehead = L.node('twelve', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    idx = 0
    flag = thellist.delete_item_at_index( idx)
    result = flag 
    assert result is True, 'delete_item_at_index() returned False for list size 2 (index = 0)'


def test_delete_item_at_index_multiple_data_1():
    thetail = L.node('ten')
    thehead = L.node('twelve', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    idx = 0
    flag = thellist.delete_item_at_index( idx)
    result = thellist._head.data
    assert result == 'ten', 'delete_item_at_index() value not deleted correctly for list size 2 (index = 0)'


def test_delete_item_at_index_multiple_size_1():
    thetail = L.node('ten')
    thehead = L.node('twelve', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    idx = 0
    flag = thellist.delete_item_at_index( idx)
    result = thellist._size 
    assert result == 1, 'delete_item_at_index() set incorrect size for list size 2'


def test_delete_item_at_index_multiple_refs_1():
    thetail = L.node('ten')
    thehead = L.node('twelve', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    idx = 0
    flag = thellist.delete_item_at_index( idx)
    result = thellist._head 
    assert result == thellist._tail, 'delete_item_at_index() head tail should be equal'


def test_delete_item_at_index_multiple_flag_2():
    thetail = L.node('ten')
    thehead = L.node('twelve', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    idx = 1
    flag = thellist.delete_item_at_index( idx)
    result = flag 
    assert result is True, 'delete_item_at_index() returned False for list size 2 (index = 0)'


def test_delete_item_at_index_multiple_data_2():
    thetail = L.node('ten')
    thehead = L.node('twelve', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    idx = 1
    flag = thellist.delete_item_at_index( idx)
    result = thellist._head.data
    assert result == 'twelve', 'delete_item_at_index() value not deleted correctly for list size 2 (index = 0)'


def test_delete_item_at_index_multiple_size_2():
    thetail = L.node('ten')
    thehead = L.node('twelve', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    idx = 1
    flag = thellist.delete_item_at_index( idx)
    result = thellist._size 
    assert result == 1, 'delete_item_at_index() set incorrect size for list size 2'


def test_delete_item_at_index_multiple_refs_2():
    thetail = L.node('ten')
    thehead = L.node('twelve', thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail
    idx = 1
    flag = thellist.delete_item_at_index( idx)
    result = thellist._head 
    assert result == thellist._tail, 'delete_item_at_index() head tail should be equal'


###############################################################################################
# INTEGRATION TESTING
###############################################################################################

###############################################################################################
# check if all the operations work after a bunch of data is added using add_to_back()
#

def test_integration_add_to_back_is_empty():
    # an integration test tests how operations work together
    # first set up a list with a bunch of nodes in the node chain

    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)

    # now check if a single aspect worked properly
    result = thellist.is_empty()
    assert result is False, "checking is_empty() after add_to_back(); returned True!"


def test_integration_add_to_back_size():
    # identical set up
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)

    # check different aspect
    assert thellist.size() == 7, "should have size 7"


def test_integration_add_to_back_value_is_in():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    assert thellist.value_is_in("HEY") is True, "should have found HEY"


def test_integration_add_to_back_value_is_in_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    assert thellist.value_is_in("STOPSIGN") is True, "should have found STOPSIGN"


def test_integration_add_to_back_value_is_in_3():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    assert thellist.value_is_in("TURTLE") is True, "should have found TURTLE"


def test_integration_add_to_back_value_is_in_4():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    assert thellist.value_is_in("not in the list") is False, "should have returned False"


def test_integration_add_to_back_get_index_of_value_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    assert thellist.get_index_of_value("HEY") == (True, 0), "HEY is at index zero"


def test_integration_add_to_back_get_index_of_value_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    assert thellist.get_index_of_value("TURTLE") == (True, 6), "TURTLE is at index 6"


def test_integration_add_to_back_get_index_of_value_3():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    assert thellist.get_index_of_value("DOING-DOING") == (True, 4), "DOING-DOING is at index 4"


def test_integration_add_to_back_get_index_of_value_4():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    assert thellist.get_index_of_value("GLOBE") == (False, None), "GLOBE Not in llist"


def test_integration_add_to_back_retrieve_data_at_index_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    assert thellist.retrieve_data_at_index( 6) == (True, "TURTLE"), "TURTLE is at index 6"


def test_integration_add_to_back_retrieve_data_at_index_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    assert thellist.retrieve_data_at_index( 0) == (True, "HEY"), "HEY is at index 0"


def test_integration_add_to_back_retrieve_data_at_index_3():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    assert thellist.retrieve_data_at_index( 2) == (True, "THANK-YOU"), "THANK-YOU is at index 2"


def test_integration_add_to_back_retrieve_data_at_index_4():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    assert thellist.retrieve_data_at_index( 7) == (False, None), "index not valid"


###############################################################################################
# check if all the operations work after a bunch of data is added using add_to_front()
#

def test_integration_add_to_front_is_empty():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_front(word)
    assert thellist.is_empty() is False, "should not be empty"


def test_integration_add_to_front_size():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_front(word)
    assert thellist.size() == 7, "should have size 7"


def test_integration_add_to_front_value_is_in_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_front(word)
    assert thellist.value_is_in("HEY") is True, "should have found HEY last"


def test_integration_add_to_front_value_is_in_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_front(word)
    assert thellist.value_is_in("STOPSIGN") is True, "should have found STOPSIGN"


def test_integration_add_to_front_value_is_in_3():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_front(word)
    assert thellist.value_is_in("TURTLE") is True, "should have found TURTLE first"


def test_integration_add_to_front_value_is_in_4():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_front(word)
    assert thellist.value_is_in("not in the list") is False, "should have returned False"


def test_integration_add_to_front_get_index_of_value_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_front(word)
    assert thellist.get_index_of_value("HEY") == (True, 6), "HEY is at index 6"


def test_integration_add_to_front_get_index_of_value_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_front(word)
    assert thellist.get_index_of_value("TURTLE") == (True, 0), "TURTLE is at index 0"


def test_integration_add_to_front_get_index_of_value_3():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_front(word)
    assert thellist.get_index_of_value("DOING-DOING") == (True, 2), "DOING-DOING is at index 2"


def test_integration_add_to_front_get_index_of_value_4():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_front(word)
    assert thellist.get_index_of_value("GLOBE") == (False, None), "GLOBE Not in llist"


def test_integration_add_to_front_retrieve_data_at_index_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_front(word)
    assert thellist.retrieve_data_at_index( 0) == (True, "TURTLE"), "TURTLE is at index 0"


def test_integration_add_to_front_retrieve_data_at_index_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_front(word)
    assert thellist.retrieve_data_at_index( 6) == (True, "HEY"), "HEY is at index 6"


def test_integration_add_to_front_retrieve_data_at_index_3():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_front(word)
    assert thellist.retrieve_data_at_index( 3) == (True, "TURN-AROUND"), "TURN-AROUND is at index 3"


def test_integration_add_to_front_retrieve_data_at_index_4():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_front(word)
    assert thellist.retrieve_data_at_index( 7) == (False, None), "index not valid"


###############################################################################################
# check what happens if you change the data in the Llist using set_data_at_index()

def test_integration_set_data_check_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    assert thellist.set_data_at_index( 0, "now") is True, "index valid"


def test_integration_set_data_get_index_of_value_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.set_data_at_index( 0, "now")
    assert thellist.get_index_of_value("HEY") == (False, None), "'HEY' should be gone"


def test_integration_set_data_get_index_of_value_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.set_data_at_index( 0, "now")
    assert thellist.get_index_of_value("now") == (True, 0), "'now' should be at index 0"


def test_integration_set_data_get_index_of_value_3():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.set_data_at_index( 0, "now")
    assert thellist.get_index_of_value("STOPSIGN") == (True, 1), "'STOPSIGN' should be still at index 1"


def test_integration_set_data_get_index_of_value_4():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.set_data_at_index( 0, "now")
    assert thellist.get_index_of_value("TURTLE") == (True, 6), "'TURTLE' should be still at index 6"


def test_integration_set_data_size_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.set_data_at_index( 0, "now")
    assert thellist.size() == 7, "should have size 7"


def test_integration_set_data_get_index_of_check_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    assert thellist.set_data_at_index( 6, "SIGN") is True, "index valid"


def test_integration_set_data_get_index_of_value_5():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.set_data_at_index( 6, "SIGN")
    assert thellist.get_index_of_value("TURTLE") == (False, None), "TURTLE should be gone"


def test_integration_set_data_get_index_of_value_6():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.set_data_at_index( 6, "SIGN")
    assert thellist.get_index_of_value("SIGN") == (True, 6), ": SIGN is at index 6"


def test_integration_set_data_get_index_of_value_7():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.set_data_at_index( 6, "SIGN")
    assert thellist.get_index_of_value("HEY") == (True, 0), "HEY is still at index 0"


def test_integration_set_data_get_index_of_value_8():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.set_data_at_index( 6, "SIGN")
    assert thellist.get_index_of_value("HORSESHOE") == (True, 5), "HORSESHOE is still at index 5"


def test_integration_set_data_get_index_of_size_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.set_data_at_index( 6, "SIGN")
    assert thellist.size() == 7, "should have size 7"


def test_integration_set_data_get_index_of_check_3():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    assert thellist.set_data_at_index( 3, "FOLLOWER") is True, ": index valid"


def test_integration_set_data_get_index_of_value_9():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.set_data_at_index( 3, "FOLLOWER")
    assert thellist.get_index_of_value("TURN-AROUND") == (False, None), "TURN-AROUND should be gone"


def test_integration_set_data_get_index_of_value_10():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.set_data_at_index( 3, "FOLLOWER")
    assert thellist.get_index_of_value("FOLLOWER") == (True, 3), "FOLLOWER is at index 3"


def test_integration_set_data_get_index_of_size_3():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.set_data_at_index( 3, "FOLLOWER")
    assert thellist.size() == 7, "should have size 7"


###############################################################################################
# check what happens as a bunch of insert_value_at() operations are used on a LList

def test_integration_insert_value_at_index_check_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    assert thellist.insert_value_at_index( "LEFT", 0) is True, "index valid"


def test_integration_insert_value_at_index_get_index_of_value_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.insert_value_at_index( "LEFT", 0)
    assert thellist.get_index_of_value("LEFT") == (True, 0), "LEFT is first"


def test_integration_insert_value_at_index_get_index_of_value_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.insert_value_at_index( "LEFT", 0)
    assert thellist.get_index_of_value("DOING-DOING") == (True, 5), "DOING-DOING is at index 5"


def test_integration_insert_value_at_index_size_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.insert_value_at_index( "LEFT", 0)
    assert thellist.size() == 8, "should have size 8"


def test_integration_insert_value_at_index_check_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.insert_value_at_index( "LEFT", 0)
    assert thellist.insert_value_at_index( "RIGHT", 8) is True, "index valid"


def test_integration_insert_value_at_index_get_index_of_value_3():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.insert_value_at_index( "LEFT", 0)
    thellist.insert_value_at_index( "RIGHT", 8)
    assert thellist.get_index_of_value("RIGHT") == (True, 8), "RIGHT is last"


def test_integration_insert_value_at_index_get_index_of_value_4():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.insert_value_at_index( "LEFT", 0)
    thellist.insert_value_at_index( "RIGHT", 8)
    assert thellist.get_index_of_value("TURTLE") == (True, 7), "TURTLE is at index 7"


def test_integration_insert_value_at_index_size_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.insert_value_at_index( "LEFT", 0)
    thellist.insert_value_at_index( "RIGHT", 8)
    assert thellist.size() == 9, ": should have size 9"


def test_integration_insert_value_at_index_check_3():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.insert_value_at_index( "LEFT", 0)
    thellist.insert_value_at_index( "RIGHT", 8)
    assert thellist.insert_value_at_index( "MIDDLE", 5) is True, "index valid"


def test_integration_insert_value_at_index_get_index_of_value_5():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.insert_value_at_index( "LEFT", 0)
    thellist.insert_value_at_index( "RIGHT", 8)
    thellist.insert_value_at_index( "MIDDLE", 5)
    assert thellist.get_index_of_value("MIDDLE") == (True, 5), "MIDDLE is at index 5"


def test_integration_insert_value_at_index_get_index_of_value_6():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.insert_value_at_index( "LEFT", 0)
    thellist.insert_value_at_index( "RIGHT", 8)
    thellist.insert_value_at_index( "MIDDLE", 5)
    assert thellist.get_index_of_value("TURTLE") == (True, 8), "TURTLE is at index 8"


def test_integration_insert_value_at_index_size_4():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.insert_value_at_index( "LEFT", 0)
    thellist.insert_value_at_index( "RIGHT", 8)
    thellist.insert_value_at_index( "MIDDLE", 5)
    assert thellist.size() == 10, "should have size 10"


###############################################################################################
# check what happens when you start deleting values from the LList

def test_integration_delete_item_at_index_check_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    assert thellist.delete_item_at_index( 0) is True, "index valid"


def test_integration_delete_item_at_index_get_index_of_value_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.delete_item_at_index( 0)
    assert thellist.get_index_of_value("HEY") == (False, None), "HEY should be gone"


def test_integration_delete_item_at_index_value_is_in_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.delete_item_at_index( 0)
    assert thellist.value_is_in("HEY") is False, "HEY should be gone"


def test_integration_delete_item_at_index_size_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.delete_item_at_index( 0)
    assert thellist.size() == 6, "should have size 6"


def test_integration_delete_item_at_index_get_index_of_value_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.delete_item_at_index( 0)
    assert thellist.get_index_of_value("STOPSIGN") == (True, 0), "STOPSIGN should be at index 0"


def test_integration_delete_item_at_index_check_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.delete_item_at_index( 0)
    assert thellist.delete_item_at_index( 5) is True, "index valid"


def test_integration_delete_item_at_index_get_index_of_value_3():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.delete_item_at_index( 0)
    thellist.delete_item_at_index( 5)
    assert thellist.get_index_of_value("TURTLE") == (False, None), "TURTLE should be gone"


def test_integration_delete_item_at_index_value_is_in_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.delete_item_at_index( 0)
    thellist.delete_item_at_index( 5)
    assert thellist.value_is_in("TURTLE") is False, "TURTLE should be gone"


def test_integration_delete_item_at_index_size_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.delete_item_at_index( 0)
    thellist.delete_item_at_index( 5)
    assert thellist.size() == 5, "should have size 5"


def test_integration_delete_item_at_index_get_index_of_value_4():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.delete_item_at_index( 0)
    thellist.delete_item_at_index( 5)
    assert thellist.get_index_of_value("HORSESHOE") == (True, 4), "HORSESHOE should be at index 4"


def test_integration_delete_item_at_index_check_3():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.delete_item_at_index( 0)
    thellist.delete_item_at_index( 5)
    assert thellist.delete_item_at_index( 2) is True, "index valid"


def test_integration_delete_item_at_index_get_index_of_value_5():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.delete_item_at_index( 0)
    thellist.delete_item_at_index( 5)
    thellist.delete_item_at_index( 2)
    assert thellist.get_index_of_value("TURN-AROUND") == (False, None), "TURN-AROUND should be gone"


def test_integration_delete_item_at_index_value_is_in_3():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.delete_item_at_index( 0)
    thellist.delete_item_at_index( 5)
    thellist.delete_item_at_index( 2)
    assert thellist.value_is_in("TURN-AROUND") is False, "TURN-AROUND should be gone"


def test_integration_delete_item_at_index_size_3():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.delete_item_at_index( 0)
    thellist.delete_item_at_index( 5)
    thellist.delete_item_at_index( 2)
    assert thellist.size() == 4, "should have size 4"


def test_integration_delete_item_at_index_get_index_of_value_6():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    thellist.delete_item_at_index( 0)
    thellist.delete_item_at_index( 5)
    thellist.delete_item_at_index( 2)
    assert thellist.get_index_of_value("DOING-DOING") == (True, 2), "DOING-DOING should be at index 2"


###############################################################################################
# check what happens when you add and remove a bunch from the back

def test_integration_remove_from_back_size():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    for i in range(4):
        thellist.remove_from_back()
    assert thellist.size() == 3, "should have size 3"


def test_integration_remove_from_back_get_index_of_value_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    for i in range(4):
        thellist.remove_from_back()
    assert thellist.get_index_of_value("TURN-AROUND") == (False, None), "TURN-AROUND should be gone"


def test_integration_remove_from_back_get_index_of_value_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    for i in range(4):
        thellist.remove_from_back()
    assert thellist.get_index_of_value("THANK-YOU") == (True, 2), "THANK-YOU should be at index 2"


def test_integration_remove_from_back_retrieve_data_at_index_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_back(word)
    for i in range(4):
        thellist.remove_from_back()
    assert thellist.retrieve_data_at_index( 2) == (True, "THANK-YOU"), "THANK-YOU is at index 2"


###############################################################################################
# check what happens when you add and remove a bunch from the front

def test_integration_remove_from_front_size():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_front(word)
    for i in range(4):
        thellist.remove_from_front()
    assert thellist.size() == 3, "should have size 3"


def test_integration_remove_from_front_get_index_of_value_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_front(word)
    for i in range(4):
        thellist.remove_from_front()
    assert thellist.get_index_of_value("TURN-AROUND") == (False, None), "TURN-AROUND should be gone"


def test_integration_remove_from_front_get_index_of_value_2():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_front(word)
    for i in range(4):
        thellist.remove_from_front()
    assert thellist.get_index_of_value("THANK-YOU") == (True, 0), "THANK-YOU should be at index 0"


def test_integration_remove_from_front_retrieve_data_at_index_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.add_to_front(word)
    for i in range(4):
        thellist.remove_from_front()
    assert thellist.retrieve_data_at_index( 0) == (True, "THANK-YOU"), "THANK-YOU is at index 0"



# a list of references to the functions defined above
all_of_em = [
    test_create_initial_size,
    test_create_initial_head,
    test_create_initial_tail,
    test_empty_empty,
    test_empty_singleton,
    test_size_singleton,
    test_add_to_front_size_1,
    test_add_to_front_head_1,
    test_add_to_front_tail_1,
    test_add_to_front_refs_1,
    test_add_to_front_data_1,
    test_add_to_front_data_2,
    test_add_to_front_end_1,
    test_add_to_front_empty_1,
    test_add_to_front_size_2,
    test_add_to_front_head_2,
    test_add_to_front_tail_2,
    test_add_to_front_refs_2,
    test_add_to_front_data_3,
    test_add_to_front_chain_2,
    test_add_to_front_chain_3,
    test_add_to_front_data_4,
    test_add_to_front_empty_2,
    test_add_to_front_size_3,
    test_add_to_back_head_1,
    test_add_to_back_tail_1,
    test_add_to_back_size_1,
    test_add_to_back_refs_1,
    test_add_to_back_data_1,
    test_add_to_back_data_2,
    test_add_to_back_chain_1,
    test_add_to_back_empty_1,
    test_add_to_back_size_2,
    test_add_to_back_size_3,
    test_add_to_back_head_2,
    test_add_to_back_tail_2,
    test_add_to_back_tail_3,
    test_add_to_back_refs_2,
    test_add_to_back_data_3,
    test_add_to_back_data_4,
    test_add_to_back_chain_2,
    test_add_to_back_empty_2,
    test_add_to_back_size_4,
    test_value_is_in_empty,
    test_value_is_in_false_1,
    test_value_is_in_true_1,
    test_value_is_in_false_2,
    test_value_is_in_true_2,
    test_value_is_in_true_3,
    test_get_index_of_value_empty_flag_1,
    test_get_index_of_value_empty_idx_1,
    test_get_index_of_value_notempty_flag_1,
    test_get_index_of_value_notempty_idx_1,
    test_get_index_of_value_notempty_flag_2,
    test_get_index_of_value_notempty_idx_2,
    test_get_index_of_value_notempty_flag_3,
    test_get_index_of_value_notempty_idx_3,
    test_get_index_of_value_notempty_flag_4,
    test_get_index_of_value_notempty_idx_4,
    test_get_index_of_value_notempty_flag_5,
    test_get_index_of_value_notempty_idx_5,
    test_retrieve_data_at_flag_1,
    test_retrieve_data_at_val_1,
    test_retrieve_data_at_flag_2,
    test_retrieve_data_at_val_2,
    test_retrieve_data_at_flag_3,
    test_retrieve_data_at_val_3,
    test_retrieve_data_at_flag_4,
    test_retrieve_data_at_val_4,
    test_retrieve_data_at_flag_5,
    test_retrieve_data_at_val_5,
    test_set_data_at_index_empty,
    test_set_data_at_index_notempty_flag_1,
    test_set_data_at_index_notempty_data_1,
    test_set_data_at_index_notempty_flag_2,
    test_set_data_at_index_notempty_data_2,
    test_set_data_at_index_notempty_flag_3,
    test_set_data_at_index_notempty_data_3,
    test_set_data_at_index_notempty_flag_4,
    test_set_data_at_index_notempty_data_4,
    test_set_data_at_index_notempty_data_5,
    test_remove_from_front_empty_1,
    test_remove_from_front_empty_2,
    test_remove_from_front_singleton_in_flag_1,
    test_remove_from_front_singleton_in_val_1,
    test_remove_from_front_singleton_in_size_1,
    test_remove_from_front_singleton_in_ref_head_1,
    test_remove_from_front_singleton_in_ref_tail_1,
    test_remove_from_front_notempty_in_flag_2,
    test_remove_from_front_notempty_in_val_2,
    test_remove_from_front_notempty_in_size_2,
    test_remove_from_front_notempty_in_ref_head_2,
    test_remove_from_front_notempty_in_ref_tail_2,
    test_remove_from_back_empty_flag,
    test_remove_from_back_empty_val,
    test_remove_from_back_singleton_flag,
    test_remove_from_back_singleton_val,
    test_remove_from_back_singleton_size,
    test_remove_from_back_singleton_in_ref_head_1,
    test_remove_from_back_singleton_in_ref_tail_1,
    test_remove_from_back_multiple_flag,
    test_remove_from_back_multiple_val,
    test_remove_from_back_multiple_size,
    test_remove_from_back_multiple_in_ref_head_2,
    test_remove_from_back_multiple_in_ref_tail_2,
    test_insert_value_at_index_empty_flag,
    test_insert_value_at_index_empty_size,
    test_insert_value_at_index_empty_refs,
    test_insert_value_at_index_empty_data_1,
    test_insert_value_at_index_empty_data_2,
    test_insert_value_at_index_empty_chain,
    test_insert_value_at_index_singleton_flag,
    test_insert_value_at_index_singleton_data,
    test_insert_value_at_index_singleton_chain_1,
    test_insert_value_at_index_singleton_size,
    test_insert_value_at_index_singleton_refs_1,
    test_insert_value_at_index_singleton_refs_2,
    test_insert_value_at_index_singleton_flag_2,
    test_insert_value_at_index_singleton_data_2,
    test_insert_value_at_index_singleton_data_3,
    test_insert_value_at_index_singleton_chain_3,
    test_insert_value_at_index_singleton_size_2,
    test_insert_value_at_index_singleton_refs_3,
    test_insert_value_at_index_singleton_chain_2,
    test_insert_value_at_index_singleton_invalid_flag,
    test_insert_value_at_index_singleton_invalid_size,
    test_insert_value_at_index_singleton_invalid_refs,
    test_insert_value_at_index_multiple_flag_1,
    test_insert_value_at_index_multiple_data_1,
    test_insert_value_at_index_multiple_size_1,
    test_insert_value_at_index_multiple_chain_1,
    test_insert_value_at_index_multiple_flag_2,
    test_insert_value_at_index_multiple_data_2,
    test_insert_value_at_index_multiple_data_3,
    test_insert_value_at_index_multiple_size_2,
    test_insert_value_at_index_multiple_chain_2,
    test_insert_value_at_index_flag_3,
    test_insert_value_at_index_data_4,
    test_insert_value_at_index_data_5,
    test_insert_value_at_index_data_6,
    test_insert_value_at_index_size_3,
    test_insert_value_at_index_chain_3,
    test_delete_item_at_index_empty_flag,
    test_delete_item_at_index_empty_size,
    test_delete_item_at_index_empty_refs,
    test_delete_item_at_index_singleton_flag,
    test_delete_item_at_index_singleton_head,
    test_delete_item_at_index_singleton_size,
    test_delete_item_at_index_singleton_tail,
    test_delete_item_at_index_multiple_flag_1,
    test_delete_item_at_index_multiple_data_1,
    test_delete_item_at_index_multiple_size_1,
    test_delete_item_at_index_multiple_refs_1,
    test_delete_item_at_index_multiple_flag_2,
    test_delete_item_at_index_multiple_data_2,
    test_delete_item_at_index_multiple_size_2,
    test_delete_item_at_index_multiple_refs_2,
    test_integration_add_to_back_is_empty,
    test_integration_add_to_back_size,
    test_integration_add_to_back_value_is_in,
    test_integration_add_to_back_value_is_in_2,
    test_integration_add_to_back_value_is_in_3,
    test_integration_add_to_back_value_is_in_4,
    test_integration_add_to_back_get_index_of_value_1,
    test_integration_add_to_back_get_index_of_value_2,
    test_integration_add_to_back_get_index_of_value_3,
    test_integration_add_to_back_get_index_of_value_4,
    test_integration_add_to_back_retrieve_data_at_index_1,
    test_integration_add_to_back_retrieve_data_at_index_2,
    test_integration_add_to_back_retrieve_data_at_index_3,
    test_integration_add_to_back_retrieve_data_at_index_4,
    test_integration_add_to_front_is_empty,
    test_integration_add_to_front_size,
    test_integration_add_to_front_value_is_in_1,
    test_integration_add_to_front_value_is_in_2,
    test_integration_add_to_front_value_is_in_3,
    test_integration_add_to_front_value_is_in_4,
    test_integration_add_to_front_get_index_of_value_1,
    test_integration_add_to_front_get_index_of_value_2,
    test_integration_add_to_front_get_index_of_value_3,
    test_integration_add_to_front_get_index_of_value_4,
    test_integration_add_to_front_retrieve_data_at_index_1,
    test_integration_add_to_front_retrieve_data_at_index_2,
    test_integration_add_to_front_retrieve_data_at_index_3,
    test_integration_add_to_front_retrieve_data_at_index_4,
    test_integration_set_data_check_1,
    test_integration_set_data_get_index_of_value_1,
    test_integration_set_data_get_index_of_value_2,
    test_integration_set_data_get_index_of_value_3,
    test_integration_set_data_get_index_of_value_4,
    test_integration_set_data_size_1,
    test_integration_set_data_get_index_of_check_2,
    test_integration_set_data_get_index_of_value_5,
    test_integration_set_data_get_index_of_value_6,
    test_integration_set_data_get_index_of_value_7,
    test_integration_set_data_get_index_of_value_8,
    test_integration_set_data_get_index_of_size_2,
    test_integration_set_data_get_index_of_check_3,
    test_integration_set_data_get_index_of_value_9,
    test_integration_set_data_get_index_of_value_10,
    test_integration_set_data_get_index_of_size_3,
    test_integration_insert_value_at_index_check_1,
    test_integration_insert_value_at_index_get_index_of_value_1,
    test_integration_insert_value_at_index_get_index_of_value_2,
    test_integration_insert_value_at_index_size_1,
    test_integration_insert_value_at_index_check_2,
    test_integration_insert_value_at_index_get_index_of_value_3,
    test_integration_insert_value_at_index_get_index_of_value_4,
    test_integration_insert_value_at_index_size_2,
    test_integration_insert_value_at_index_check_3,
    test_integration_insert_value_at_index_get_index_of_value_5,
    test_integration_insert_value_at_index_get_index_of_value_6,
    test_integration_insert_value_at_index_size_4,
    test_integration_delete_item_at_index_check_1,
    test_integration_delete_item_at_index_get_index_of_value_1,
    test_integration_delete_item_at_index_value_is_in_1,
    test_integration_delete_item_at_index_size_1,
    test_integration_delete_item_at_index_get_index_of_value_2,
    test_integration_delete_item_at_index_check_2,
    test_integration_delete_item_at_index_get_index_of_value_3,
    test_integration_delete_item_at_index_value_is_in_2,
    test_integration_delete_item_at_index_size_2,
    test_integration_delete_item_at_index_get_index_of_value_4,
    test_integration_delete_item_at_index_check_3,
    test_integration_delete_item_at_index_get_index_of_value_5,
    test_integration_delete_item_at_index_value_is_in_3,
    test_integration_delete_item_at_index_size_3,
    test_integration_delete_item_at_index_get_index_of_value_6,
    test_integration_remove_from_back_size,
    test_integration_remove_from_back_get_index_of_value_1,
    test_integration_remove_from_back_get_index_of_value_2,
    test_integration_remove_from_back_retrieve_data_at_index_1,
    test_integration_remove_from_front_size,
    test_integration_remove_from_front_get_index_of_value_1,
    test_integration_remove_from_front_get_index_of_value_2,
    test_integration_remove_from_front_retrieve_data_at_index_1
    ]


runemall()

