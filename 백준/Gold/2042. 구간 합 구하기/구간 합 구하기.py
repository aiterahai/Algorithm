from sys import stdin

N,M,K = map(int,stdin.readline().split())
board = [int(stdin.readline().strip()) for _ in range(N)]
tree = [0 for _ in range(4 * len(board))]

def init(start, end, index):
    if start == end:
        tree[index] = board[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = init(start, mid, index*2) + init(mid+1, end, index*2+1)
    return tree[index]

def interval_sum(start, end, index, left, right):
    if left > end or right < start : return 0
    if left <= start and end <= right : return tree[index]
    mid = (start + end) // 2
    return interval_sum(start,mid,index*2,left,right) + interval_sum(mid+1,end,index*2+1,left,right)

def update(start,end,index,targetindex, diff):
    if targetindex < start or targetindex > end : return
    tree[index] += diff
    if start == end : return
    mid = (start + end) // 2
    update(start, mid, index * 2, targetindex, diff)
    update(mid+1, end, index * 2 + 1, targetindex, diff)

init(0,N-1,1)

for _ in range(M+K):
    a,b,c = map(int,stdin.readline().split())
    if a == 1 :
        diff = c - board[b - 1]
        board[b - 1] = c
        update(0,N-1,1,b-1,diff)

    if a == 2 :
        print(interval_sum(0,N-1,1,b-1,c-1))