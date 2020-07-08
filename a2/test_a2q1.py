import unittest
import a2q1

# Test harness for walkers
class TestCalcWalk(unittest.TestCase):
    testData = [  ['L L L', 3],             ['R L L', 1],
                  ['R R L', 1],             ['R R R', 3],
                  ['asdfsadseesdf', 0],     ['U', 0],
                  ['R L L R', 0],           ['L R R L R', 1]]

    # verify a single pair
    def test_single_walk(self):
        for inp, out in self.testData:
            self.assertEqual(a2q1.getDistance(inp, ('L', 'R')), out)

    # verify list of pairs
    def test_double_walk(self):
        pairs = [('L', 'R'), ('U', 'D')]
        out = {"U/D": 0, "L/R": 0}
        self.assertEqual(a2q1.calcWalk("L R U D", pairs), out)
