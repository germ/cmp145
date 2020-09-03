# Jeremy Bernhardt, jrb569, 11119747, CMPT 145: 2020ST2
import unittest
import exampletrees as t

import A9Q2 as a2
import A9Q1 as a1

class TestMirror(unittest.TestCase):
  def test_none(self):
    self.assertTrue(a2.mirrored(None, None))
    self.assertFalse(a2.mirrored(t.ctree, None))
    self.assertFalse(a2.mirrored(None, t.ctree))
  
  def test_singleton(self):
    # Test against same tree
    self.assertTrue(a2.mirrored(t.ctree, t.ctree))

    # Test against modified
    v = a1.copy(t.ctree)
    a1.subst(v, 'si', 'yee')
    self.assertFalse(a2.mirrored(v, t.ctree))

  def test_multi(self):
    # Test against same tree
    self.assertTrue(a2.mirrored(t.expr_tree, t.expr_tree))

    # Test against modified
    v = a1.copy(t.expr_tree)
    a1.subst(v, '*', '_')
    a1.subst(v, '.', '^')
    self.assertFalse(a2.mirrored(v, t.expr_tree))

# Run all tests
if __name__ == '__main__':
    unittest.main()