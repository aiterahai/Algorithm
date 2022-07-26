from sys import stdin
import heapq

Q = []
for _ in range(int(stdin.readline())):
    arr = list(map(int, stdin.readline().split()))
    if not Q:
        for a in arr:
            heapq.heappush(Q, a)
        continue
    for a in arr:
        if Q[0] < a:
            heapq.heappush(Q, a)
            heapq.heappop(Q)
print(Q[0])