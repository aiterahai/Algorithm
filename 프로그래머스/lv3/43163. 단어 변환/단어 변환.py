from collections import deque

def solution(begin, target, words):
    words += [begin]
    answer = 0
    board = [[diff(i, j) for i in words] for j in words]
    visit = [-1] * len(words)
    visit[-1] = 0
    if target not in words: return 0
    Q = deque()
    Q.append(len(words) - 1)
    while Q:
        x = Q.popleft()
        for i in range(len(words)):
            if not board[x][i]: continue
            if visit[i] != -1: continue
            Q.append(i)
            visit[i] = visit[x] + 1
    print(visit)
    return visit[words.index(target)] 

def diff(A, B):
    count = 0
    for i, j in zip(A, B):
        if i == j: continue
        count += 1
    return 1 if count == 1 else 0