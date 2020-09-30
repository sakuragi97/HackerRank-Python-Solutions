# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

phonebook = {}
for i in range(n):
    string = input()
    strlist = string.split(sep=' ')
    phonebook[strlist[0]] = strlist[1]

search="0"
while search!='':
    try:
        search = input()
        if search in phonebook:
            print (f"{search}={phonebook.get(search)}")
        else:
            print("Not found")
    except EOFError:
        break
