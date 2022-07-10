from sys import stdin

result = [0, 0, 0]
def paper(N, board, x, y):
    global result
    for i in [-1, 0, 1]:
        ifbreak = False
        for j in range(x, x + N):
            for k in range(y, y + N):
                if board[j][k] != i:
                    ifbreak = True
                    break
                if j == x + N - 1 and k == y + N - 1:
                    result[i+1] += 1
                    return
            if ifbreak: break

    t = N // 3
    for i in range(x, x + N, t):
        for j in range(y, y + N, t):
            paper(t, board, i, j)

N = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for i in range(N)]
paper(N, board, 0, 0)
for i in result: print(i)