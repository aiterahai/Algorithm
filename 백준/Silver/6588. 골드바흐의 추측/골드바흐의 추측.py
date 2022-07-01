from sys import stdin
from math import sqrt

# 에라토스테네스의 체
K = int(sqrt(1000000)) + 1
board = [True] * (1000001)
board[0], board[1] = False, False
for i in range(2, K):
    if not board[i]: continue
    for j in range(2 * i, 1000001, i):
        if j > 1000000: break
        board[j] = False
primes = [i for i, j in enumerate(board) if j]
length = len(primes)
primes.append(10000000000)

def binary_search(N, start, end):
    middle = (start + end) // 2
    if primes[middle + 1] > N >= primes[middle]: return middle
    if N > primes[middle]: return binary_search(N, middle + 1, end)
    return binary_search(N, start, middle - 1)

# 투 포인터
while True:
    N = int(stdin.readline())
    if not N: break
    start, end = 1, binary_search(N, 1, length - 1)
    while True:
        temp = primes[start] + primes[end]
        if temp < N:
            start += 1
        elif temp > N:
            end -= 1
        else:
            print(f"{N} = {primes[start]} + {primes[end]}")
            break