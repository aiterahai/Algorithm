from sys import stdin
arr = list(map(int, stdin.readline().split()))
a, b = min(arr), max(arr)
if(a == b):
    print(0)
    exit(0)
print(b-a-1)
for i in range(a+1, b): print(i, end=" ")