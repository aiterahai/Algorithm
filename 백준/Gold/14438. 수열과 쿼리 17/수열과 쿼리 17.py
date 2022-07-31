from sys import stdin

def init(node, start, end):
    if start == end:
        tree[node] = board[start]
        return tree[node]
    tree[node] = min(init(node * 2, start, (start + end) // 2), init(node * 2 + 1, (start + end) // 2 + 1, end))
    return tree[node]

def update(node, start, end, index, value):
    if start > index or end < index: return
    if start == end:
        tree[node] = value
        return
    update(node * 2, start, (start + end) // 2, index, value)
    update(node * 2 + 1, (start + end) // 2 + 1, end, index, value)
    tree[node] = min(tree[node * 2], tree[node * 2 + 1])

def sub(node, start, end, left, right):
    if left > end or right < start: return int(1e10)
    if left <= start and end <= right: return tree[node]
    return min(sub(node * 2, start, (start + end) // 2, left, right),
               sub(node * 2 + 1, (start + end) // 2 + 1, end, left, right))

N = int(stdin.readline())
board = list(map(int, stdin.readline().split()))
tree = [0] * N * 4
init(1, 0, N - 1)
for _ in range(int(stdin.readline())):
    A, B, C = map(int, stdin.readline().split())
    if A == 1:
        board[B - 1] = C
        update(1, 0, N - 1, B - 1, C)
    else: print(sub(1, 0, N - 1, B - 1, C - 1))