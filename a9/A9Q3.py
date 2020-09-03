# Jeremy Bernhardt, jrb569, 11119747, CMPT 145: 2020ST2

def complete(t):  
  """
    Calculate the tree is a full binary tree
    Pre-conditions:
        t:  The tree to be checked
    Returns
      True if valid binary tree, False otherwise
  """
  def cmplt(t):
    """
      Helper func that is called recursively
      Calculates the height and checks for binary validity
      Pre-conditions:
          t:  The tree to be checked
      Returns
        (Boolean, Int) Tuple representing the validity and height of the tree
    """
    # Hit bottom of tree
    if t is None:
      return (True, 0)
    # Compare lengths of deeper segments
    else:
      bin1, ldepth = cmplt(t.left)
      bin2, rdepth = cmplt(t.right)
      if ldepth == rdepth and bin1 and bin2:
        return (True, rdepth + 1)
      else:
        return (False, rdepth + 1)

  # Run helper on tree, check for height
  bal, h = cmplt(t)
  if bal and h > 0:
    return True
  return False