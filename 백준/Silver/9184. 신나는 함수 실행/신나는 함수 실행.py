from sys import stdin

def w(A, B, C):
    if min(A, B, C) <= 0: return 1
    if max(A, B, C) > 20: return w(20, 20, 20)
    if dp[A][B][C]: return dp[A][B][C]
    if A < B < C: dp[A][B][C] = w(A, B, C - 1) + w(A, B - 1, C - 1) - w(A, B - 1, C); return dp[A][B][C]
    dp[A][B][C] = w(A - 1, B, C) + w(A-1, B-1, C) + w(A-1, B, C-1) - w(A-1, B-1, C-1); return dp[A][B][C]

dp = [[[0 for i in range(21)] for i in range(21)] for i in range(21)]

while True:
    A, B, C = map(int, stdin.readline().split())
    if A == B == C == -1: break
    print(f"w({A}, {B}, {C}) = {w(A, B, C)}")