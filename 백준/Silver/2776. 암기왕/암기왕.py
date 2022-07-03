from sys import stdin

def binary_search(board, j, start, end):
    middle = (start + end) // 2
    if board[middle] == j: return 1
    elif start > end: return 0
    elif board[middle] > j: return binary_search(board, j, start, middle - 1)
    elif board[middle] < j: return binary_search(board, j, middle + 1, end)

T = int(stdin.readline())
for i in range(T):
    N = int(stdin.readline())
    board = sorted(list(map(int, stdin.readline().split())))
    M = int(stdin.readline())
    for j in list(map(int, stdin.readline().split())):
        print(binary_search(board, j, 0, N-1))