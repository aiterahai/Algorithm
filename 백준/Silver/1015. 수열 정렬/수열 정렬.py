from sys import stdin

N = int(stdin.readline())
board = list(map(int, stdin.readline().split()))
sorted_board = sorted(board)
for i in range(N):
    temp = sorted_board.index(board[i])
    sorted_board[temp] = 9999
    print(temp, end=" ")