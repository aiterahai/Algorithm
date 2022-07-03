from sys import stdin
from collections import Counter

N = int(stdin.readline())
S = Counter([stdin.readline()[:-1] for i in range(N)])
C = Counter([stdin.readline()[:-1] for i in range(N-1)])
S.subtract(C)
for i in S:
    for j in range(S[i]):
        print(i)