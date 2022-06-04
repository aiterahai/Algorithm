from sys import stdin
n = int(stdin.readline())
a = sorted(map(int, stdin.readline().split()))
b = sorted(map(int, stdin.readline().split()), reverse=True)
sum = 0
for i in range(n):
    sum += a[i]*b[i]
print(sum)