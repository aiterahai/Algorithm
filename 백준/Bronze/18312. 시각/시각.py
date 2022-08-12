from sys import stdin

N, K = map(int, stdin.readline().split())
print(sum(1 for i in range(0, N + 1) for j in range(0, 60) for k in range(0, 60) if f"{i:02d}{j:02d}{k:02d}".find(str(K)) != -1))