from sys import stdin
n = int(stdin.readline())
arr = [list(input().split()) for _ in range(n)]
for i in range(n):
    arr[i][0] = int(arr[i][0])
arr = sorted(arr, key=lambda x:(x[0]))
for a, b in arr:
    print(a, b)