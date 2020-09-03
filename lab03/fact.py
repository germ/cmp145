# fact.py
# version 2

import sys 


def factorial(x):
    """
    Calculate  the  product  of  numbers 1 to x.8
    """
    total = 1
    for i in range(1,x+1):
        total  *= i
    return  total

if len(sys.argv) == 1:
    print("Usage: fact.py [positive int]")
    exit(-1)

print(factorial(int(sys.argv[1])))
