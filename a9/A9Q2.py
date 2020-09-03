# Jeremy Bernhardt, jrb569, 11119747, CMPT 145: 2020ST2

import A9Q1 as t

def mirrored(a, b):
  """
  Calculate if the data in trees a and b satisfy the mirror property
    Pre-conditions:
        a:  The first TreeNode to be compared
        b:  The second TreeNode to be compared
    Returns
      True if satisfied, False otherwise
  """
  # Handle empty trees
  if a == None and b == None:
    return True
  if (a and b == None) or (b and a == None):
    return False

  # Check if value of current nodes match
  if a.data != b.data:
    return False
  
  # Check leaves
  if mirrored(a.left, b.left) and mirrored(a.right, b.right):
    return True
  return False