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
#    Demo script for A8

import A8Q1
import A8Q4
import A8Q3
import A8Q2
import node as N

# demo for to_string()
example3 = N.Node(1, N.Node(2, N.Node(3)))
example2 = N.Node(1)
example1 = None
print("Here's an empty node-chain:", A8Q1.to_string(example1))
print("Here's a node-chain with one node:", A8Q1.to_string(example2))
print("Here's a node-chain with three nodes:", A8Q1.to_string(example3))

# demo for randchain
example4 = A8Q1.randchain(5, range(10))
print("Here's a node-chain with 5 random nodes:", A8Q1.to_string(example4))

# demo for insert_chain
example16 = None
node1 = N.Node(3)
print("An empty node chain:", A8Q1.to_string(example16))
print("A node:", A8Q1.to_string(node1))
example17 = A8Q2.insert_node(node1, example16)
print("After insert_chain():", A8Q1.to_string(example17))

example16 = N.Node(4)
node1 = N.Node(3)
print("A singleton node chain:", A8Q1.to_string(example16))
print("A node:", A8Q1.to_string(node1))
example17 = A8Q2.insert_node(node1, example16)
print("After insert_chain():", A8Q1.to_string(example17))

example16 = N.Node(1)
node1 = N.Node(3)
print("A singleton node chain:", A8Q1.to_string(example16))
print("A node:", A8Q1.to_string(node1))
example17 = A8Q2.insert_node(node1, example16)
print("After insert_chain():", A8Q1.to_string(example17))

example14 = N.Node(1, N.Node(2, N.Node(4)))
node1 = N.Node(3)
print("A node chain, increasing order:", A8Q1.to_string(example14))
print("A node:", A8Q1.to_string(node1))
example15 = A8Q2.insert_node(node1, example14)
print("After insert_chain():", A8Q1.to_string(example15))

# demo for sort_chain
example7 = A8Q1.randchain(7, range(5))
print("Input node chain:", A8Q1.to_string(example7))
example8 = A8Q2.sort_chain(example7)
print("Sorted node chain:", A8Q1.to_string(example8))

# demo for split_chain
example9 = N.Node(1, N.Node(3, N.Node(4, N.Node(2, N.Node(3, N.Node(6))))))
print("Starting node_chain:", A8Q1.to_string(example9))
lc, ec, gc = A8Q3.split_chain(3, example9)
print("Resulting lesser chain:", A8Q1.to_string(lc))
print("Resulting equal chain:", A8Q1.to_string(ec))
print("Resulting greater chain:", A8Q1.to_string(gc))

# demo for extend_chain:
example11 = N.Node(1, N.Node(3))
example12 = N.Node(4, N.Node(5))
print("An increasing node_chain:", A8Q1.to_string(example11))
print("Another increasing node_chain:", A8Q1.to_string(example12))
example13 = A8Q3.extend_chain(example11, example12)
print("After extend_chain():", A8Q1.to_string(example13))

# demo for sort_chain
example7 = A8Q1.randchain(7, range(5))
print("Input node chain:", A8Q1.to_string(example7))
example8 = A8Q3.sort_chain(example7)
print("Sorted node chain:", A8Q1.to_string(example8))

# demo for A8Q4.split_chain
example5 = A8Q1.randchain(5, range(10))
print("Starting node-chain:", A8Q1.to_string(example5))
left, right = A8Q4.split_chain(example5)
print("After split_chain, left:", A8Q1.to_string(left))
print("After split_chain, right:", A8Q1.to_string(right))

# demo for merge_chain
left = N.Node(1, N.Node(3, N.Node(4)))
right = N.Node(2, N.Node(3, N.Node(6)))
print("One node chain in increasing order:", A8Q1.to_string(left))
print("Another node chain in increasing order:", A8Q1.to_string(right))
example6 = A8Q4.merge_chain(left, right)
print("Two node chains merged:", A8Q1.to_string(example6))

# demo for sort_chain
example7 = A8Q1.randchain(7, range(5))
print("Input node chain:", A8Q1.to_string(example7))
example8 = A8Q4.sort_chain(example7)
print("Sorted node chain:", A8Q1.to_string(example8))



