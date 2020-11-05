#!/bin/python3

import re
from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    emailDict = defaultdict(list)
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        emailDict[firstName].append(emailID)


gmailEmail=[]
for data in sorted(emailDict):
    if len(emailDict[data]) >= 2:
        for i in range(len(emailDict[data])):
            popElement = emailDict[data].pop()
            if re.search(r'[a-z.]{2,50}@gmail.com', popElement):
                gmailEmail.append(data)
        continue
    popElement = emailDict[data].pop()
    if re.search(r'[a-z.]{2,50}@gmail.com',popElement):
        gmailEmail.append(data)

for i in gmailEmail:
    print(i)