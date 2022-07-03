from sys import stdin

N, M = map(int, stdin.readline().split())
board = list(map(int, stdin.readline().split()))
arr = [0]

for i in board:
    arr.append(arr[-1] + i)
for i in range(M):
    T = list(map(int, stdin.readline().split()))
    print(arr[T[1]] - arr[T[0] - 1])