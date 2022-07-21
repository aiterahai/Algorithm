from sys import stdin
from collections import deque

visit = [0 for _ in range(101)]
ladder = [i for i in range(101)]
for _ in range(sum(map(int, stdin.readline().split()))):
    A, B = map(int, stdin.readline().split())
    ladder[A] = B

Q = deque([1])
visit[1] = 1
while Q:
    node = Q.popleft()
    for i in range(1, 7):
        nextnode = node + i
        if nextnode > 100: continue
        nextnode = ladder[nextnode]
        if visit[nextnode]: continue
        visit[nextnode] = visit[node] + 1
        Q.append(nextnode)
print(visit[100] - 1)