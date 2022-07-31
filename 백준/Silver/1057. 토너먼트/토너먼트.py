from sys import stdin

K, N, M = map(int, stdin.readline().split())
count = 0
while N != M:
    N, M = (N + 1) // 2, (M + 1) // 2
    count += 1
print(count)