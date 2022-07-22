from sys import stdin

N, M, K = map(int,stdin.readline().split())
board = [int(stdin.readline().strip()) for _ in range(N)]
tree = [0 for _ in range(4 * len(board))]

def init(start, end, index):
    if start == end:
        tree[index] = board[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = init(start, mid, index*2) * init(mid+1, end, index*2+1) % 1000000007
    return tree[index]

def interval_multi(start, end, index, left, right):
    if left > end or right < start : return 1
    if left <= start and end <= right : return tree[index]
    mid = (start + end) // 2
    return interval_multi(start,mid,index*2,left,right) * interval_multi(mid+1,end,index*2+1,left,right) % 1000000007

def update(start,end,index, where, diff):
    if where < start or where > end : return
    if start == end : tree[index] = diff; return
    mid = (start + end) // 2
    update(start, mid, index * 2, where, diff)
    update(mid + 1, end, index * 2 + 1, where, diff)
    tree[index] = tree[2 * index] * tree[2 * index + 1] % 1000000007

init(0,N-1,1)

for _ in range(M+K):
    A, B, C = map(int,stdin.readline().split())
    if A == 1:
        update(0, N - 1, 1, B - 1, C)
    else:
        print(interval_multi(0,N-1,1,B-1,C-1))