from sys import stdin

def binary_search(start, end, M):
    middle = (start + end) // 2
    temp = sum([min(middle, i) for i in board])
    if temp == M or start > end: return middle
    if temp < M: return binary_search(middle + 1, end, M)
    if temp > M: return binary_search(start, middle - 1, M)

N = int(stdin.readline())
board = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
print(max(board) if sum(board) <= M else binary_search(1, 10000000000, M))