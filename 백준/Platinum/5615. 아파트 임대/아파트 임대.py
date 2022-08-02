from sys import stdin

def isPrime(N, i):
    r, d = 0, N - 1
    while not(d % 2): r, d = r + 1, d // 2
    x = pow(i, d, N)
    if x == 1 or x == N - 1: return 1
    for _ in range(0, r - 1):
        x = pow(x, 2, N)
        if x == N - 1: return 1
    return 0

answer, board = 0, [2, 3, 5, 7, 11]
for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    count = 0
    for i in board: count += isPrime(2*N+1, i)
    if count == len(board): answer += 1
print(answer)