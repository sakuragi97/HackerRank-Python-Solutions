# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt, floor

def isPrime(a):
    if a==1:
        return False
    for i in range(2,floor(sqrt(a))+1):
        if a%i==0:
            return False
    return True


T = int(input())
listIntegers = list()
while T!=0:
    n = int(input())
    listIntegers.append(n)
    T-=1
for i in listIntegers:
    if isPrime(i):
        print('Prime')
    else:
        print('Not prime')