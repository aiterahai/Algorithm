from sys import stdin
n = int(stdin.readline())
count = n
for i in range(n):
    temp = stdin.readline()
    for j in range(len(temp)):
        if temp[j] in temp[j+1:] and temp[j] != temp[j+1]:
            count -= 1
            break
print(count)