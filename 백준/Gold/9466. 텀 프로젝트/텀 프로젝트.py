"""
file name: 9466.py

create time: 2023-04-18 10:08
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin, setrecursionlimit
setrecursionlimit(int(1e5))

def dfs(node):
    visit[node] = True
    cycle.append(node)
    next = board[node]

    if visit[next]:
        if next in cycle:
            return len(cycle[cycle.index(next):])
        return 0

    return dfs(next)

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    board = [0] + list(map(int, stdin.readline().split()))
    visit = [False for _ in range(N + 1)]
    result = 0
    for i in range(1, N + 1):
        if visit[i]: continue
        cycle = []
        result += dfs(i)

    print(N - result)