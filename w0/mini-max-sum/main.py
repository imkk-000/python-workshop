#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(list):
    sumOfList = sum(list)
    maximumNumber = 0
    minimumNumber = 4000000001
    for elm in list:
        diffSum = sumOfList - elm
        if maximumNumber < diffSum:
            maximumNumber = diffSum
        if minimumNumber > diffSum:
            minimumNumber = diffSum
    print("{} {}".format(minimumNumber, maximumNumber))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
