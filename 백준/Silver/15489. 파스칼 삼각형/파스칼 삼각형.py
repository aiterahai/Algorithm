board = [[0 for _ in range(100)] for _ in range(100)]
board[0][0] = 1
for i in range(1, 100):
    for j in range(i + 1):
        board[i][j] = board[i-1][j] + board[i-1][j - 1]
R, C, W = map(int, input().split())
answer = 0
for i in range(W):
    for j in range(i + 1): answer += board[R+i-1][C+j-1]
print(answer)