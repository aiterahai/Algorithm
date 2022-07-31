from sys import stdin

def init(node, start, end):
    if start == end:
        tree[node] = board[start]
        return tree[node]
    tree[node] = min(init(node * 2, start, (start + end) // 2), init(node * 2 + 1, (start + end) // 2 + 1, end))
    return tree[node]

def minsub(node, start, end, left, right):
    if left > end or start > right: return int(1e10)
    if left <= start and end <= right: return tree[node]
    return min(minsub(node * 2, start, (start + end) // 2, left, right), minsub(node * 2 + 1, (start + end) // 2 + 1, end, left, right))



N, M = map(int, stdin.readline().split())
board = [int(stdin.readline()) for _ in range(N)]
tree = [0] * 4 * N
init(1, 0, N - 1)
for _ in range(M):
    A, B = map(int, stdin.readline().split())
    print(minsub(1, 0, N - 1, A - 1, B - 1))