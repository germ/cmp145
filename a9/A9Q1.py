# Jeremy Bernhardt, jrb569, 11119747, CMPT 145: 2020ST2

import treenode as t

def subst(tree, t, r):
    """
    Substitutes a target value for r in the Tree
    Pre-conditions:
        tree: The node tree to preform the operation on
        t: A target value to be replaced
        r: The value to replace it with
    Post-conditions:
        t is replaced by r for all nodes in the Tree
    Returns:
        None
    """

    # Empty Tree
    if tree == None or t == None or r == None:
        return None

    # Try replacing val
    if tree.data == t:
        tree.data = r
        return 

    # Recurse
    if tree.left:
        return subst(tree.left, t, r)

    if tree.right:
        return subst(tree.right, t, r)

def copy(tree):
    """
    Makes a new copy of the tree
    Pre-conditions:
        tree: The node tree to preform the operation on
    Returns:
        A tree object with the same values as the original
    """
    # Sanity check
    if tree == None:
        return None

    # Recurse, making new objs
    ret = t.treenode(tree.data)
    if tree.left:
        ret.left = copy(tree.left)
    if tree.right:
        ret.right = copy(tree.right)
    
    return ret

def collect_data_inorder(tree):
    """
    Collapse tree to a in-order list
    Pre-conditions:
        tree: The node tree to preform the operation on
    Returns:
        A list containing all values in the tree
    """
    # Base case
    if tree == None:
        return []
    
    # Recurse through tree
    ret = []
    if tree.left:
        ret.extend(collect_data_inorder(tree.left))
    ret.append(tree.data)
    if tree.right:
        ret.extend(collect_data_inorder(tree.right))

    return ret

def count_smaller(tree, target):
    """
    Counts all values less then target in a tree
    Pre-conditions:
        tree: The node tree to preform the operation on
        target: The value to compare against
    Returns:
        (int) The number of values found that are less then target
        None on nonnumeric
    """
    # Check for empty tree
    if tree == None or target == None:
        return None

    # Check for nonnumeric in root
    if not (type(tree.data) is int or type(tree.data) is float):
        return None

    # Recurse through tree
    ret = 0
    if tree.left:
        ret += count_smaller(tree.left, target)
    if tree.right:
        ret += count_smaller(tree.right, target)
    # Check for numeric types, excl complex
    if tree.data < target:
        ret += 1

    return ret