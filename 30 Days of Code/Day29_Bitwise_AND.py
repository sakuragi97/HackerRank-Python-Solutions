#!/bin/python3

# def findBitwise(n,k):
#     maxBitwise=0
#     i=0
#     j=i+1
#     for i in range(n-1):
#         for j in range(n):
#             if i&j>maxBitwise and i&j<k:
#                 maxBitwise=i&j
#     print(maxBitwise)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        if (k-1|k)<=n:
            print(k-1)
        else:
            print(k-2)