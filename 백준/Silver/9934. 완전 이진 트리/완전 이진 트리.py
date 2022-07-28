from sys import stdin

def func(start, end, K):
    if not K: return
    mid = (start + end) // 2
    result[K-1].append(board[mid])
    func(start, mid - 1, K-1)
    func(mid + 1, end, K-1)

K = int(stdin.readline())
result = [[] for i in range(K)]
board = list(map(int, stdin.readline().split()))
func(0, 2 ** K - 1, K)
for i in range(K - 1, -1, -1): print(*result[i])