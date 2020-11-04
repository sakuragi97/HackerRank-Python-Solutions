# Enter your code here. Read input from STDIN. Print output to STDOUT


def calculateFine(r,e):
    if r[1]==e[1] and r[2]==e[2]:
        if r[0]-e[0]<=0:
            return 0
        else:
            return 15 * (r[0]-e[0])
    elif r[2]==e[2]:
        if r[1]-e[1]<=0:
            return 0
        else:
            return 500 * (r[1]-e[1])
    else:
        if r[2] - e[2] <= 0:
            return 0
        else:
            return 10000


returnedDay = input().split(sep=' ')
returnedDay = [int(i) for i in returnedDay]
expectedDay = input().split(sep=' ')
expectedDay = [int(i) for i in expectedDay]

print(calculateFine(returnedDay,expectedDay))
