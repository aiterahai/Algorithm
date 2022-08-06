from sys import stdin

def binary_search(start, end):
    mid = (start + end) // 2
    if mid == 0: return 0
    if start > end: return mid
    if sum([i // mid for i in board]) >= N: return binary_search(mid + 1, end)
    return binary_search(start, mid - 1)

N, M = map(int, stdin.readline().split())
board = list(map(int, stdin.readline().split()))
print(binary_search(0, max(board)))