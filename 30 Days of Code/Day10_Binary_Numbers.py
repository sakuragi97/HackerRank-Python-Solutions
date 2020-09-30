#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())

binary = "{0:b}".format(n)

countlist = []
counter = 0
for i in range(len(binary)):
    if binary[i] == '1':
        counter += 1
    elif binary[i] == '0':
        if counter != 0:
            countlist.append(counter)
        counter = 0
countlist.append(counter)
maxcounter = max(countlist)
print(maxcounter)
