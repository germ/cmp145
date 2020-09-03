# Jeremy Bernhardt, jrb569, 11119747, CMPT 145: 2020ST2
import unittest
import treenode as t
import A9Q3 as a

class TestComplete(unittest.TestCase):
  def test_empty(self):
    self.assertFalse(a.complete(None))

  def test_singleton(self):
    v = t.treenode(1)
    self.assertTrue(a.complete(v))

  def test_multiple(self):
    balTree   = t.treenode(1, t.treenode(2), t.treenode(3))
    unbalTree = t.treenode(1, t.treenode(2), t.treenode(3, t.treenode(4)))
    lopsidedTree = t.treenode(1, t.treenode(1, t.treenode(1)), t.treenode(1))

    self.assertTrue(a.complete(balTree))
    self.assertFalse(a.complete(unbalTree))
    self.assertFalse(a.complete(lopsidedTree))

 # Run all tests
if __name__ == '__main__':
    unittest.main()   