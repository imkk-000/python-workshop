#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    chars = list(s)
    def countWithFilter(lists, target): return len(
        list(filter(lambda ch: target == ch, lists)))
    newList = [(ch, countWithFilter(chars, ch)) for ch in set(chars)]
    newList = sorted(newList, key=lambda l: l[0])
    newList = sorted(newList, key=lambda l: l[1], reverse=True)
    newList = newList[:3]

    for ch, counter in newList:
        print(ch, counter)
