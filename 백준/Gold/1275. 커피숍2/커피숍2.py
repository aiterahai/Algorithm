from sys import stdin

def init(node, start, end):
    if start == end:
        tree[node] = board[start]
        return tree[node]
    tree[node] = init(node * 2, start, (start + end) // 2) + init(node * 2 + 1, (start + end) // 2 + 1, end)
    return tree[node]

def sub(node, start, end, left, right):
    if left > end or start > right: return 0
    if left <= start and end <= right: return tree[node]
    return sub(node * 2, start, (start + end) // 2, left, right) + sub(node * 2 + 1, (start + end) // 2 + 1, end, left, right)

def change(node, start, end, index, diff):
    if index < start or end < index: return
    tree[node] += diff
    if start != end:
        change(node * 2, start, (start + end) // 2, index, diff)
        change(node * 2 + 1, (start + end) // 2 + 1, end, index, diff)

N, Q = map(int, stdin.readline().split())
board = list(map(int, stdin.readline().split()))
tree = [0] * N * 4
init(1, 0, N - 1)
for _ in range(Q):
    A, B, C, D = map(int, stdin.readline().split())
    if A > B: B, A = A, B
    print(sub(1, 0, N - 1, A - 1, B - 1))
    diff = D - board[C - 1]
    board[C - 1] = D
    change(1, 0, N - 1, C - 1, diff)