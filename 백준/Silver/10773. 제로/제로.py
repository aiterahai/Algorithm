from sys import stdin
arr = []
for i in range(int(stdin.readline())):
    temp = int(stdin.readline())
    if(temp): arr.append(temp)
    else: arr.pop()
print(sum(arr))