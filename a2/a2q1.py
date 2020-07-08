# Jeremy Bernhardt, jrb569, 11119747, CMPT 145: 2020ST2
# a2q1: Module for processing walks

import sys
from typing import List, Tuple, Dict
 
def calcWalk(walk: str, pairs: List[Tuple[str, str]]) -> (Dict[str, int]):
    """   Calculate the distances for a list of axis on a given walk-string

          walk:   The input to parse
          pairs:  List of tuples for walk axis (L, R), (U, D), etc

          returns: 
            Dict[str, int] with entries for each axis and total computed
    """
    # Define return storage
    ret: Dict[str, int] = {}

    # Loop and fill return data
    for axis in pairs:
        ret[f"{axis[0]}/{axis[1]}"] = getDistance(walk, axis)

    # return to caller
    return ret

def getDistance(src: str, axis: Tuple[str, str]) -> int:
    """
      Calculate the distance for a single axis on in a input string

      src:  The input string to be processed for walk
      axis: Tuple containing pairs to count

      returns:
        absolute value of difference
    """
    return abs(src.count(axis[0]) - src.count(axis[1]))


# Main logic
if __name__ == '__main__':
    # Check if files are supplied
    if len(sys.argv) == 1:
        print("Usage: ./a2q1.py inputfile inputfile inputfile...")
        exit()
    
    # define axis to use
    axis: List[Tuple[str, str]] = [('L', 'R')]

    # Loop over system args
    for fName in sys.argv[1:]:
        # Attempt open, exit on failure
        try:
            with open(fName) as f:
                print(f"Processing: {fName}")
                # Pass off each line to be calculated, display output
                for line in f.readlines():
                    # Display in cannonical way for single pairs
                    if len(axis) == 1:
                        for v in calcWalk(line, axis).values():
                            print(v)

                    # verbose output for multi-axis
                    else:
                        print(calcWalk(line, axis))

        except OSError:
            print(f"Could not open file {fName}, exiting.")
            exit()
