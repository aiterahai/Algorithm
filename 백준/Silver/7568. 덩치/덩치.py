from sys import stdin
n = int(stdin.readline())
rank = [1 for i in range(n)]
arr = []
for i in range(n):
    arr.append(list(map(int, stdin.readline().split())))
for i in range(n):
    for j in range(n):
        if(arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]):
            rank[i] += 1

for i in rank:
    print(i, end=" ")