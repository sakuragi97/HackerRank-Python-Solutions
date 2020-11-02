#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here


def swap(a,b):
    a,b = b,a
    return a,b


totalNumberOfSwaps = 0
for i in range(len(a)):
    numberOfSwaps = 0
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = swap(a[j],a[j+1])
            numberOfSwaps += 1
    totalNumberOfSwaps += numberOfSwaps
    if numberOfSwaps == 0:
        break

print(f'Array is sorted in {totalNumberOfSwaps} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[n-1]}')