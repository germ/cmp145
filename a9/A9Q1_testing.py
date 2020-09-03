# Jeremy Bernhardt, jrb569, 11119747, CMPT 145: 2020ST2
import unittest
from A9Q1 import collect_data_inorder
import exampletrees as t
import treefunctions as f
import treenode as n
import A9Q1 as a

class TestSubst(unittest.TestCase):
  def test_empty(self):
    v = a.copy(t.fibonatree)

    # Preform a bunch of ops that should short early
    a.subst(None,None,None)
    a.subst(v,1,None)
    a.subst(v,None,1)
    a.subst(None,1,1)
    self.assertTrue(f.to_string(v) == f.to_string(t.fibonatree))

  def test_singleton(self):
    tree = a.copy(t.ctree)
    a.subst(tree, 'si', 'yee')
    self.assertFalse(f.to_string(tree) == f.to_string(t.ctree))

  def test_larger(self):
    v = a.copy(t.xtree)
    a.subst(v, 1, 2)
    self.assertTrue(a.count_smaller(v, 1) == 0)

  def test_nonexist(self):
    v = a.copy(t.ctree)
    a.subst(v, 999, 999)
    self.assertTrue(a.collect_data_inorder(v) == ['si'])

class TestCopy(unittest.TestCase):
  def test_empty(self):
    v = None
    t = a.copy(v)
    self.assertTrue(f.to_string(v) == f.to_string(t))

  def test_singleton(self):
    v = a.copy(t.ctree)
    self.assertTrue(f.to_string(v) == f.to_string(t.ctree))
    self.assertFalse(id(v) == id(t.ctree))

  def test_larger(self):
    v = a.copy(t.xtree)
    self.assertTrue(f.to_string(v) == f.to_string(t.xtree))
    self.assertFalse(id(v) == id(t.ctree))

  def test_largest(self):
    v = a.copy(t.fibonatree)
    self.assertTrue(f.to_string(v) == f.to_string(t.fibonatree))
    self.assertFalse(id(v) == id(t.ctree))

class TestCollect(unittest.TestCase):
  def test_empty(self):
    self.assertTrue(a.collect_data_inorder(None) ==  [])

  def test_singleton(self):
    v = t.ctree
    self.assertTrue(a.collect_data_inorder(v) == ['si'])

  def test_larger(self):
    v = t.xtree
    # Output from xTree, verified by hand
    exp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 1, 3]
    self.assertTrue(a.collect_data_inorder(v) == exp)

class TestSmaller(unittest.TestCase):
  def test_empty(self):
    # Input garunteed to be numeric
    self.assertTrue(a.count_smaller(None, 1) == None)
    self.assertTrue(a.count_smaller(t.ctree, None) == None)

  def test_nonnumeric(self):
    self.assertTrue(a.count_smaller(t.ctree, 5) == None)
    self.assertTrue(a.count_smaller(t.expr_tree, 5) == None)
  
  def test_counts(self):
    self.assertTrue(a.count_smaller(t.fibonatree, 2) == 11)
    self.assertTrue(a.count_smaller(t.fibonatree, -1) == 0)
    self.assertTrue(a.count_smaller(t.xtree, 5) == 7)
  
  def test_singleton(self):
    v = n.treenode(1)
    self.assertTrue(a.count_smaller(v, 5) == 1)
    self.assertTrue(a.count_smaller(v, 0) == 0)
    self.assertTrue(a.count_smaller(v, -1) == 0)

# Run all tests
if __name__ == '__main__':
    unittest.main()