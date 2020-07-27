# CMPT 145 Course material
# Copyright (C) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this 
# file to a public or private website, or providing this file to a person 
# not registered in CMPT 145, constitutes Academic Misconduct, according 
# to the University of Saskatchewan Policy on Academic Misconduct.
# 
# Synopsis:
#    SOme functions to test.

# Jeremy Bernhardt, jrb569, 11119747, CMPT 145: 2020ST2

def newtonraphson(x):
    """ Compute sqrt using iterative method

    args: 
        x: Number to root (numeric) 
    return: 
        The computed root (numeric)
    """
    root = 1
    while abs(x - root * root) > 0.00001:
        root = (x/root + root) / 2.0
    return root
 
def gcd(a, b):
    """ Compute the greatest common divisor of two numbers

    args:
        a, b: numbers to factor (numeric)
    return:
        the greatest common factor (numeric)
    
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def read_triangle(filename):
    """ Read in a pascal triangle from a formatted data file

    args: 
        filename: Path to the data to be loaded
    return:
        Tuple with the size of the triangle and list containing the triangle
    """
    file = open(filename)
    triangle = []
    for line in file:
        line = line.rstrip().split()
        line = [int(d) for d in line]
        triangle.append(line)
    file.close()
    size = triangle[0][0]
    triangle = triangle[1:]
    return (size, triangle)

def remdup(alist):
    """ Remove any duplicate items from a list
    args: alist
        The list to be modified and deduplicated
    effects:
        The argument is modified not copied
    return:
        None
    
    Notes: For lists with more then two duplicates, program crashes. See
    test cases for more information
    """
    alist.reverse()
    for i in range(len(alist)-1):
        while alist[i] in alist[i+1:]:
            del alist[i]
    alist.reverse()
