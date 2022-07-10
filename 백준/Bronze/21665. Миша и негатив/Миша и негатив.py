N, M = map(int, input().split())
board = [input() for i in range(N)]
input()
board_2 = [input() for i in range(N)]
count = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == board_2[i][j]:
            count += 1
print(count)