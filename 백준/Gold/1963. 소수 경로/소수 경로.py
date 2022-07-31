from sys import stdin
from collections import deque

def diff(A, B):
    return sum([A[i] == B[i] for i in range(4)])

check_prime = [True] * 10000
check_prime[0], check_prime[1] = False, False
for i in range(2, int(10000 ** 0.5) + 1):
    if not check_prime[i]: continue
    for j in range(i ** 2, 10000, i):
        check_prime[j] = False
prime = [i for i in range(1000, 10000) if check_prime[i]]
board = [[] for i in range(10000)]
for i in prime:
    for j in prime:
        if diff(str(i), str(j)) == 3: board[i].append(j)

for _ in range(int(stdin.readline())):
    visit = [0] * 10000
    A, B = map(int, stdin.readline().split())
    Q = deque([A])
    visit[A] = 1
    while Q:
        node = Q.popleft()
        for i in board[node]:
            if visit[i]: continue
            Q.append(i)
            visit[i] = visit[node] + 1
    print(visit[B] - 1 if visit[B] else "Impossible")