#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'xo' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING s as parameter.
#
def xo(s):
    newStr = s.lower()
    if newStr.find("x") == newStr.find("o") == -1:
        return True
    return newStr.count("x") == newStr.count("o")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = xo(s)

    fptr.write(str(int(result)) + '\n')

    fptr.close()
