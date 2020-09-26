# Enter your code here. Read input from STDIN. Print output to STDOUT


def eve_odd(string):
    even = []
    odd = []
    for s in range(len(string)):

        if s % 2 == 0:
            even.append(string[s])
        else:
            odd.append(string[s])
    print("".join(even), "".join(odd), sep=' ')


string = []
i = int(input())
for i in range(i):
    string.append(input())

for i in range(len(string)):
    eve_odd(string[i])
