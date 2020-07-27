# CMPT 145: Assignment 5 Question 3
# test script

import a5q1 as a5q1
import a5q3 as a5q3
import node as N




####################################################################################################
#### UNIT TEST CASE: check_chains() ####
test_item = "check_chains()"

data_in1 = None
data_in2 = None
expected = 'same chain'
reason = 'Two empty node chains'

result = a5q3.check_chains(data_in1, data_in2)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))

#### UNIT TEST CASE: check_chains() ####
data_in1 = N.node(1)
data_in2 = None
expected = 'different'
reason = 'One empty node chain'

result = a5q3.check_chains(data_in1, data_in2)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))

#### UNIT TEST CASE: check_chains() ####
data_in1 = None
data_in2 = N.node(1)
expected = 'different'
reason = 'One empty node chain'

result = a5q3.check_chains(data_in1, data_in2)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))


#### UNIT TEST CASE: check_chains() ####
data_in1 = N.node(1)
data_in2 = N.node(1)
expected = 'same values'
reason = 'Simple node chains, same values'

result = a5q3.check_chains(data_in1, data_in2)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))


#### UNIT TEST CASE: check_chains() ####
data_in1 = N.node(1)
data_in2 = data_in1
expected = 'same chain'
reason = 'Simple node chain, two copies of the same reference'

result = a5q3.check_chains(data_in1, data_in2)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))


#### UNIT TEST CASE: check_chains() ####
data_in1 = N.node(1, N.node(2, N.node(3)))
data_in2 = data_in1
expected = 'same chain'
reason = 'longer node chain, two copies of the same reference'

result = a5q3.check_chains(data_in1, data_in2)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))

#### UNIT TEST CASE: check_chains() ####
data_in1 = N.node(1, N.node(2, N.node(3)))
data_in2 = N.node(1, N.node(2, N.node(3)))
expected = 'same values'
reason = 'longer node chain, two copies of the same chain'

result = a5q3.check_chains(data_in1, data_in2)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))

#### UNIT TEST CASE: check_chains() ####
data_in1 = N.node(1, N.node(2, N.node(3)))
data_in2 = N.node(1, N.node(2, N.node(1)))
expected = 'different'
reason = 'longer node chain, similar, last value different'

result = a5q3.check_chains(data_in1, data_in2)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))


#### UNIT TEST CASE: check_chains() ####
data_in1 = N.node(1, N.node(2, N.node(3)))
data_in2 = N.node(1, N.node(2, N.node(3, N.node(4))))
expected = 'different'
reason = 'longer node chain, similar, second chain longer'

result = a5q3.check_chains(data_in1, data_in2)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))

#### UNIT TEST CASE: check_chains() ####
data_in1 = N.node(1, N.node(2, N.node(3, N.node(4))))
data_in2 = N.node(1, N.node(2, N.node(3)))
expected = 'different'
reason = 'longer node chain, similar, first chain longer'

result = a5q3.check_chains(data_in1, data_in2)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))


#### UNIT TEST CASE: check_chains() ####
data_in1 = N.node(1, N.node(2, N.node(3, N.node(4))))
data_in2 = N.node(2, N.node(3, N.node(4)))
expected = 'different'
reason = 'longer node chain, very different'

result = a5q3.check_chains(data_in1, data_in2)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))











####################################################################################################
#### UNIT TEST CASE: copync() ####
test_item = "copync()"

data_in = None
expected = 'same chain'
reason = 'Empty node chain'

result = a5q3.check_chains(data_in, a5q3.copync(data_in))
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))


data_in = N.node(1)
expected = 'same values'
reason = 'Singleton node chain'

result = a5q3.check_chains(data_in, a5q3.copync(data_in))
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))

data_in = N.node(1, N.node(2, N.node(3)))
expected = 'same values'
reason = 'Longer node chain'

temp = a5q3.copync(data_in)
result = a5q3.check_chains(data_in, temp)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))


####################################################################################################
#### UNIT TEST CASE: copync() ####
test_item = "double_up()"

data_in = None
expected = None
reason = 'Empty node chain'

result = a5q3.double_up(data_in)
result_str = a5q1.to_string(result)
expected_str = a5q1.to_string(expected)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))


data_in = N.node('a')
expected = N.node('a', N.node('a'))
reason = 'singleton node chain'

a5q3.double_up(data_in)
result_str = a5q1.to_string(data_in)
expected_str = a5q1.to_string(expected)
if result_str != expected_str:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))


data_in = N.node('a', N.node('b', N.node('see')))
expected = N.node('a', N.node('a', N.node('b', N.node('b', N.node('see', N.node('see'))))))
reason = 'longer node chain'

a5q3.double_up(data_in)
result_str = a5q1.to_string(data_in)
expected_str = a5q1.to_string(expected)
if result_str != expected_str:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))




####################################################################################################
print('*** testing complete ***')



