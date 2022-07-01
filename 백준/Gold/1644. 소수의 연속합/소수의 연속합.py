import math
N = int(input())
K = int(math.sqrt(N)) + 1
board = [True] * (N + 1)
board[0], board[1] = False, False
for i in range(2, K):
    if not board[i]: continue
    for j in range(2 * i, N + 1, i):
        if j > N: break
        board[j] = False
primes = [i for i, j in enumerate(board) if j]
start, end, count, prefix, length = 0, 0, 0, 0, len(primes)
while True:
    if end >= length or start >= length: break
    elif prefix < N:
        prefix += primes[end]
        end += 1
    elif prefix > N:
        prefix -= primes[start]
        start += 1
    else:
        prefix = prefix + primes[end] - primes[start]
        end, start, count, = end + 1, start + 1, count + 1
if N == 1:
    print(0)
    exit(0)
elif board[N]: count += 1
print(count)