"""
file name: 1967.py

create time: 2023-04-10 22:05
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin
import sys

sys.setrecursionlimit(10 ** 5)

N = int(stdin.readline())
edge = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    p, c, w = map(int, stdin.readline().split())
    edge[p].append([c, w])
    edge[c].append([p, w])
visit = [0 for _ in range(N + 1)]

result = 0
far_node = 0
def dfs(node, k):
    if k == 0: visit[node] = 1
    global result
    global far_node
    for next, w in edge[node]:
        if visit[next]: continue
        visit[next] = 1
        dfs(next, k + w)
        visit[next] = 0
    if k > result:
        far_node = node
        result = k

dfs(1, 0)
visit[1] = 0
dfs(far_node, 0)
print(result)