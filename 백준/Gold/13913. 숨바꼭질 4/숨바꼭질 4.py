from collections import deque

N, K = map(int, input().split())
visit = [[0, 0] for i in range(100001)]
Q = deque()
Q.append(N)
visit[N][0] = 1
while Q:
    x = Q.popleft()
    for i in [x + 1, x - 1, x * 2]:
        if i < 0 or i >= 100001: continue
        if visit[i][0]: continue
        Q.append(i)
        visit[i][0] = visit[x][0] + 1
        visit[i][1] = x
print(visit[K][0] - 1)
result = []
while True:
    result.append(K)
    if K == N: break
    K = visit[K][1]
result.reverse()
print(" ".join(map(str, result)))