# Jeremy Bernhardt, jrb569, 11119747, CMPT 145: 2020ST2

def ordered(t):
  """
  Checks if a given tree is ordered
  Pre-conditions:
      t: The tree to preform the operation on
  Returns:
      True if the tree is ordered, False otherwise
  """
  # No subtrees, it's balanced!
  if t == None:
    return True

  # Check for sorted property
  if t.left and t.left.data > t.data:
    return False

  if t.right and t.right.data < t.data:
    return False

  # Recurse
  return ordered(t.left) and ordered(t.right)