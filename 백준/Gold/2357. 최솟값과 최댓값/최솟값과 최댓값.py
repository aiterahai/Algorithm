from sys import stdin

def mininit(node, start, end):
    if start == end:
        mintree[node] = board[start]
        return mintree[node]
    mintree[node] = min(mininit(node * 2, start, (start + end) // 2), mininit(node * 2 + 1, (start + end) // 2 + 1, end))
    return mintree[node]

def maxinit(node, start, end):
    if start == end:
        maxtree[node] = board[start]
        return maxtree[node]
    maxtree[node] = max(maxinit(node * 2, start, (start + end) // 2), maxinit(node * 2 + 1, (start + end) // 2 + 1, end))
    return maxtree[node]

def minsub(node, start, end, left, right):
    if left > end or start > right: return int(1e10)
    if left <= start and end <= right: return mintree[node]
    return min(minsub(node * 2, start, (start + end) // 2, left, right),
                minsub(node * 2 + 1, (start + end) // 2 + 1, end, left, right))

def maxsub(node, start, end, left, right):
    if left > end or start > right: return 0
    if left <= start and end <= right: return maxtree[node]
    return max(maxsub(node * 2, start, (start + end) // 2, left, right),
                maxsub(node * 2 + 1, (start + end) // 2 + 1, end, left, right))

N, M = map(int, stdin.readline().split())
board = [int(stdin.readline()) for _ in range(N)]
mintree = [0] * N * 4
maxtree = [0] * N * 4
mininit(1, 0, N - 1)
maxinit(1, 0, N - 1)
for _ in range(M):
    A, B = map(int, stdin.readline().split())
    print(minsub(1, 0, N - 1, A - 1, B - 1), maxsub(1, 0, N - 1, A - 1, B - 1))