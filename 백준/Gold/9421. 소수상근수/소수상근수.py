from sys import stdin

def func(N):
    if N == 1: return True
    temp = sum([int(i) ** 2 for i in str(N)])
    if visit[temp]: return False
    visit[temp] = True
    return func(temp)
N = int(stdin.readline())
board = [True] * 1000001
board[0], board[1] = False, False
for i in range(2, int(1000001 ** 0.5) + 1):
    if not board[i]: continue
    for j in range(i ** 2, 1000001, i):
        board[j] = False
prime = [i for i in range(1000001) if board[i]]
for i in prime:
    if i > N: break
    visit = [False] * 1001
    if func(i): print(i)