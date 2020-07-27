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
#   Defines the Statistics ADT
#   Calculate mean and variance and other statistical summaries  
#   of numeric data.

# Implementation
# Do the calculations without storing all the data!
# Use a Python dictionary as a record to store three quantities:
#   _count':     the number of data values added
#   _avg':       the running average of the values added

# These values can be modified every time a new data value is 
# added, so that the mean and variance can be calculated quickly  
# as needed.  This approach means that we do not need to store  
# the data values themselves, which could save a lot of space.
#
# NOTE: This file does not contain the full ADT as shown in class.  
#       The calculations for var() and sampvar() were removed to 
#       keep the exercise concise.

class Statistics(object):
    def __init__(self):
        """
        Purpose:
            Initialize a Statistics object instance.
        """
        self.__count = 0      # how many data values seen so far
        self.__avg = 0        # the running average so far
        self.__min = None     # Smallest value seen
        self.__max = None     # Largest value seen


    def add(self, value):
        """
        Purpose:
            Use the given value in the statistics calculation
        Pre-Conditions:
            :param value: the value to be added
        Post-Conditions:
            none
        Return:
            :return none
        """

        # Update count
        self.__count += 1           

        # Update mean
        k = self.__count            
        diff = value - self.__avg  
        self.__avg += diff / k
    
        # Update Min
        if self.__min == None:
            self.__min = value
        else: 
            min(self.__min, value)

        # Update Max
        if self.__max == None:
            self.__max = value
        else:
            self.__max = max(self.__max, value)

    def mean(self):
        """
        Purpose:
            Return the average of all the values seen so far.
        Post-conditions:
            (none)
        Return:
            The mean of the data seen so far.
            Note: if no data has been seen, 0 is returned.
                  This is clearly false.
        """
        return self.__avg

    def count(self):
        """
        Purpose:
            Return the number of values seen so far.
        Post-conditions:
            (none)
        Return:
            The number of values seen so far.
            Note: if no data has been seen, 0 is returned.
                  This is clearly false.
        """
        return self.__count
    
    def minimum(self):
        """
        Purpose:
            Return the smallest value seen
        Post-conditions:
            (none)
        Return:
            The smallest value seen so far, or None
        """
        return self.__min

    def maximum(self):
        """
        Purpose:
            Return the largest value seen
        Post-conditions:
            (none)
        Return:
            The largest value seen so far
            Note: if no data has been seen or None
        """
        return self.__max
