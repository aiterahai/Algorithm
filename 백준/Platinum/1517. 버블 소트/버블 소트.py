def mergesort(start, end):
    global swap, board
    if start >= end: return
    mid = (start + end) // 2
    mergesort(start, mid)
    mergesort(mid + 1, end)
    temp, a, b = [], start, mid + 1
    while a <= mid and b <= end:
        if board[a] <= board[b]: temp.append(board[a]); a += 1
        else: temp.append(board[b]); b += 1; swap += (mid - a + 1)
    if a <= mid: temp = temp + board[a:mid + 1]
    if b <= end: temp = temp + board[b:end + 1]
    for i in range(len(temp)): board[start + i] = temp[i]

swap = 0
N = int(input())
board = list(map(int, input().split()))
mergesort(0, N - 1)
print(swap)