from collections import Counter
from sys import stdin

N = int(stdin.readline())
for i in range(N):
    a, b = stdin.readline().split()
    a_cnt = Counter(a)
    b_cnt = Counter(b)
    if a_cnt == b_cnt: print("Possible")
    else: print("Impossible")