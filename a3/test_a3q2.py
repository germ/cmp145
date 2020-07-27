# Jeremy Bernhardt, jrb569, 11119747, CMPT 145: 2020ST2

import unittest
import a3q2 as a

class Testa3q2(unittest.TestCase):
    print(
"""Notes: 
A bug in a3q2.gcd will hang this test runner
A bug in a3q2.remdup will trigger a out of bounds error as well causing the tests to fail.

See test case comments for failing tests
""")
    rootTests = [(25,   5,              "Basic int gcd"), 
                 (5,    2.2360679775,   "Non-int root"), 
                 (10,   3.16227766017,  "Non-int root"), 
                 (0,    0,              "Boundary testing"),
                 (0.2,  0.4472135955,   "Floating input and output"), 
                 (0.5,  0.70710678118,  "Floating input and output"), 
                 (1,    1,              "Transition point, same In/Out")
    ]

    gcdTests = [[(5,10),    5,  "Lower arg1 higher arg2"], 
                [(10, 5),   5,  "Higher arg1 lower arg2"], 
                [(5,5),     5,  "Same arg1/arg2"], 
               #[(0,1),     1,  "Boundary case."],    # This case will cause the runner to hang
    ]

    triangleFiles = ["example.txt", "testingTriangle1.txt", "testingTriangle2.txt"]

    dupTests = [ ([],                   [],             "Empty input/Empty output"), 
                 ([1,2,3],              [1,2,3],        "Same in/out, no dups"), 
                 ([1,1,2,3],            [1,2,3],        "Single dup, repeated place"), 
                #([1,1,1],              [1],            "Multiple dups, in order."),    # Out of bounds crash
                #([1,2,3,3,4,3,5,3],    [1,2,3,4,5],    "Multiple dups, out of order"), # Out of bounds crash
    ]

    def testRoots(self):
        for i in self.rootTests:
            # Check if aproximation is near
            self.assertTrue(abs(a.newtonraphson(i[0]) - i[1]) < 0.01, i[2])
    
    def testGCD(self):
        # Loops for case [(0,1), 1]. Zero factors into every integer so
        # this edge case triggers a bug in the implementation
        for i in self.gcdTests:
            self.assertEqual(a.gcd(i[0][0], i[0][1]), i[1], i[2])

    def testTriangles(self):
        for f in self.triangleFiles:
            size, tri = a.read_triangle(f)
            
            # Test size
            self.assertTrue(len(tri) == size, "Triangle height improperly loaded.")

            # Test num of elements
            nElem   = sum([len(i) for i in tri])
            nTest   = size * (size+1)/2
            self.assertTrue(nTest == nElem, "Number of total elements improperly loaded.")

            # Test for lists
            self.assertFalse(False in [type(i) for i in tri], "Loaded data wrong type.")

    def testRemdup(self):
        # Tests fail for lists with over 2 repeating values
        for i in self.dupTests:
            a.remdup(i[0]) 
            self.assertTrue(i[0] == i[1], i[2])

# If test suite is run directly, run tests
if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().discover("./"))
