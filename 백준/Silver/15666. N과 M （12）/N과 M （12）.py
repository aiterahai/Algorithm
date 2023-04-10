"""
file name: 15663.py

create time: 2023-04-10 17:07
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin
N, M = map(int, stdin.readline().split())
board = sorted(list(map(int, stdin.readline().split())))

visit = [False] * N
sequence = []

def dfs(K):
    if K == M:
        print(*sequence)
        return
    prev = 0
    for i in range(N):
        if board[i] == prev or (sequence and board[i] < sequence[-1]): continue
        prev = board[i]
        visit[i] = True
        sequence.append(board[i])
        dfs(K + 1)
        visit[i] = False
        sequence.pop()

dfs(0)