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

import LList as L

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

    score = [(15,0), (31,5), (40,10), (52, 15), (63,20), (70,24), (85,27), (87,30)]

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
            test_integration_remove_from_back_size,
            test_integration_remove_from_back_get_index_of_value_1,
            test_integration_remove_from_back_get_index_of_value_2,
            test_integration_remove_from_front_size,
            test_integration_remove_from_front_get_index_of_value_1,
            test_integration_remove_from_front_get_index_of_value_2,
    ]


runemall()

