from sys import stdin

def quad(N, board, x, y):
    for i in ["0", "1"]:
        ifbreak = False
        for j in range(x, x + N):
            for k in range(y, y + N):
                if board[j][k] != i:
                    ifbreak = True
                    break
                if j == x + N - 1 and k == y + N - 1:
                    print(i, end="")
                    return
            if ifbreak: break

    print("(", end="")
    t = N // 2
    quad(t, board, x, y)
    quad(t, board, x, y + t)
    quad(t, board, x + t, y)
    quad(t, board, x + t, y + t)
    print(")", end="")

N = int(stdin.readline())
board = [stdin.readline()[:-1] for i in range(N)]
quad(N, board, 0, 0)