#!/bin/python3

import math
import os
import random
import re
import sys

#
# arr = [
#     [1, 1, 1, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0],
#     [1, 1, 1, 0, 0, 0],
#     [0, 0, 2, 4, 4, 0],
#     [0, 0, 0, 2, 0, 0],
#     [0, 0, 1, 2, 4, 0],
# ]

# #Displaying Matrix
# for i in range(6):
#     for j in range(6):
#         print(A[i][j],'', end='')
#     print()


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

sumlist=[]
for i in range(4):
    for j in range(4):
        sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
        sumlist.append(sum)

print(max(sumlist))