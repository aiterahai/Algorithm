from sys import stdin

N, K = map(int, stdin.readline().split())
N = N - (K+1)*K//2
if N < 0: print(-1); exit(0)
print(K-1 if N % K == 0 else K)