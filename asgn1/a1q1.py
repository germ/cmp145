# Jeremy Bernhardt, jrb569, 11119747, CMPT 145: 2020ST2
# a1q1: Verify Latin Squares

from typing import List

def verifySquare(sq: List[List[int]]) -> bool:
  """
  Verify a NxN Latin square.
  sq:       The latin square to be verified
  returns:  True if a valid square is evaluated
  """

  # Check 1: Dimensional Check, Should be square
  if len(sq) != len(sq[0]):
    return False

  # Check 2: Max-Value Check, should be in range 0-N
  # Flatten matrix, test if outside of bounds, look for any False
  if False in list(map(lambda x: x > 0 and x <= len(sq), [i for e in sq for i in e])):
    return False

  # Check 3: Row-Column Check, expression adds in a rotated matrix, removes duplicates,
  # Converts to tuples, de-duplicates rows. If more then 1 element remains it is not valid
  if 1 != len(set(list(map(tuple, 
    [set(x) for x in sq.copy() + [list(x) for x in zip(*sq[::-1])]])))):
    return False
    
  return True

#Main Program
if __name__ == "__main__":
  """
  Data is provided in three files containing formatted latin squares, 
  these files will be loaded and verified. Output will be written to stdout
  """

  # Loop over all files
  files = ["simple.txt", "examples1.txt", "examples2.txt"]
  for fName in files:
    f = open(fName)

    # Retrieve header with length of following data
    numSquares = int(f.readline())
    print(f"Checking {numSquares} examples ...")

    # Loop over square data
    for i in range(0, numSquares):
      sq:List[List[int]] = []

      # Populate square line by line
      for j in range(0, int(f.readline())):
        sq.append([int(x) for x in f.readline().rstrip().split()])
      
      # Verify and output validity
      if verifySquare(sq):
        print(f"Example  {i}: valid")
      else:
        print(f"Example  {i}: *** not  valid  ***")

      # consume blank line
      f.readline()

    # File cleanup, proceed to next
    f.close()
  
  print("Done.")
