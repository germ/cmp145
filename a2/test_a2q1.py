import unittest
import a2q1

class TestCalcWalk(unittest.TestCase):
    testData = [  ['L L L', 3],   ['R L L', 1],
                  ['R R L', 1],   ['R R R', 3],
                  ['R L L R', 0], ['L R R L R', 1]]

    def test_single_walk(self):
        for inp, out in self.testData:
            self.assertEqual(a2q1.getDistance(inp, ('L', 'R')), out)

    def test_double_walk(self):
        pairs = [('L', 'R'), ('U', 'D')]
        out = {"U/D": 0, "L/R": 0}
        self.assertEqual(a2q1.calcWalk("L R U D", pairs), out)
