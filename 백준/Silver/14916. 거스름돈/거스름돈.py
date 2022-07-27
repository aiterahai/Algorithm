from sys import stdin

N = int(stdin.readline())
temp, answer, N = N, N // 5, N % 5
while N:
    if N > temp: print(-1); exit(0)
    answer, N = answer + 1, N - 2
    if N < 0: answer, N = answer - 1, N + 5
print(answer)