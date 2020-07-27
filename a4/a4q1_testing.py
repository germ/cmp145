# Jeremy Bernhardt, jrb569, 11119747, CMPT 145: 2020ST2
# Synopsis: Assignment 3: ADTs and Testing

import Statistics as S
import unittest, sys, io

# Helper Functions
def close_enough(a, b, tolerance):
    """
    Purpose:
        Check if 2 floating point values are close enough to 
        be considered equal.  See the Addendum in the assignment!
    Pre-Conditions:
        :param a: a floating point value
        :param b: a floating point value
        :param tolerance: a small positive floating point value
    Post-Conditions:
        none
    Return:
        :return True if the difference between a and b is small
    """
    return abs(a - b) < tolerance

def isClose(a, b):
    return close_enough(a, b, 0.000001)


# Testing Begin
class TestStats(unittest.TestCase):
    # Tests are in the format ([inputs], (countResult, meanResult), ErrorMessage)
    addMeanTests = [
        ([0],           (1, 0),     "Wrong total items/mean:"),
        ([1],           (1, 1),     "Wrong total items/mean:"),
        ([1,2,3],       (3, 2),     "Wrong total items/mean:"),
        ([0,0,0,0,0],   (5, 0),     "Wrong total items/mean:"),
        ([-3,0,3],      (3, 0),     "Wrong total items/mean:"),
        ([1.0,int(2)],  (2, 1.5),   "Wrong total items/mean:"),
    ]

    # Test Creation / default values of object
    def testCreate(self):
        stats = S.Statistics()
        self.assertTrue(stats.count() == 0, "Integration: Improper initial count values.")
        self.assertTrue(stats.mean()  == 0, "Integration: Improper initial mean value.")

    # Test Add, Mean and count  methods. Because we can't inspect the values directly
    # These tests are combined and both sets of values checked. This removes code duplication
    def testAddMeanCount(self):
        for t in self.addMeanTests:
            stat = S.Statistics()
            for i in t[0]:
                stat.add(i)

            self.assertTrue(stat.count() == len(t[0]),                    f"{t}")
            self.assertTrue(isClose(stat.mean(), sum(t[0])/len(t[0])),    f"{t}")


# If test suite is run directly, run tests
if __name__ == "__main__":
    # Buffer io, redirect std err
    buf = io.StringIO()
    sys.stderr = buf

    # Run all tests
    testResults = unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover("./"))

    # Display success message or dump buffer
    if testResults.wasSuccessful():
        print("*** Test script completed ***")
    else:
        buf.seek(0)
        print(buf.read())
