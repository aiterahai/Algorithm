from sys import stdin

N = stdin.readline().rstrip()
if sum([int(i) for i in N]) % 3 != 0 or N.find("0") == -1: print(-1)
else: print(*sorted(N, reverse=True), sep="")