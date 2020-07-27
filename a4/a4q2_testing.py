# Jeremy Bernhardt, jrb569, 11119747, CMPT 145: 2020ST2
# Assignment 3: ADTs and Testing

import a4q2 as S
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
    # Tests are in the format ([inputs], (countResult, meanResult, minResult, maxResult), ErrorMessage)
    addMeanTests = [
        ([0],           (1, 0, 0, 0),                   "Wrong operation detected:"),
        ([1],           (1, 1, 1, 1),                   "Wrong operation detected:"),
        ([1,2,3],       (3, 2, 1, 3),                   "Wrong operation detected:"),
        ([0,0,0,0,0],   (5, 0, 0, 0),                   "Wrong operation detected:"),
        ([-3,0,3],      (3, 0,-3, 3),                   "Wrong operation detected:"),
        ([],            (0, 0, None, None),             "Wrong operation detected:"),
        ([1.0,int(2)],  (2, 1.5, 1, 2),                 "Wrong operation detected:"),
    ]

    # Test Creation / default values of object
    def testCreate(self):
        stats = S.Statistics()
        self.assertTrue(stats.count()     == 0,    "Improper initial count values.")
        self.assertTrue(stats.mean()      == 0,    "Improper initial mean value.")
        self.assertTrue(stats.minimum()   == None, "Improper initial min value.")
        self.assertTrue(stats.maximum()   == None,    "Improper initial max value.")


    # Test Add, Mean, Count, Min and Max  methods. 
    # These tests are combined and all sets of values checked. This removes code duplication
    def testOperations(self):
        for t in self.addMeanTests:
            stat = S.Statistics()
            for i in t[0]:
                stat.add(i)

            self.assertTrue(stat.maximum()      == t[1][3],        f"{t}")
            self.assertTrue(stat.count()        == t[1][0],        f"{t}")
            self.assertTrue(isClose(stat.mean(),   t[1][1]),       f"{t}")
            self.assertTrue(stat.minimum()      == t[1][2],        f"{t}")
            self.assertTrue(stat.maximum()      == t[1][3],        f"{t}")

# If test suite is run directly, run tests
if __name__ == "__main__":
    # Buffer io, redirect std err
    buf = io.StringIO()
    sys.stderr = buf

    # Run all tests
    tests       = unittest.TestLoader().loadTestsFromTestCase(TestStats)
    testResults = unittest.TextTestRunner(verbosity=2).run(tests)

    # Display success message or dump buffer
    if testResults.wasSuccessful():
        print("*** Test script completed ***")
    else:
        # Dump buffer to console
        buf.seek(0)
        print(buf.read())
