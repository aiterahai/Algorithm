from sys import stdin
from math import ceil

H, W, N, M = map(float, stdin.readline().split())
print(ceil(H / (N + 1)) * ceil(W / (M + 1)))