# Jeremy Bernhardt, jrb569, 11119747, CMPT 145: 2020ST2
import unittest
import exampletrees as t
from treenode import treenode as n
import A9Q4 as a

class TestComplete(unittest.TestCase):
  def test_empty(self):
    self.assertTrue(a.ordered(None))
  
  def test_singleton(self):
    self.assertTrue(a.ordered(t.ctree))

  def test_multiple(self):
    ordTree = n(7, n(5, n(1), n(6)), n(9, n(8), n(11)))
    unbalOrdTree = n(7, n(5, n(1), n(6)), n(9))

    self.assertTrue(a.ordered(ordTree))
    self.assertTrue(a.ordered(unbalOrdTree))
    self.assertFalse(a.ordered(t.fibonatree))
    self.assertFalse(a.ordered(t.expr_tree))

# Run all tests
if __name__ == '__main__':
  unittest.main()